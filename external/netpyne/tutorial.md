---
layout: default
title: "NetPyNE docs: NetPyNE チュートリアル<a href=\"#netpyne-tutorial\" class=\"headerlink\" title=\"Link to this heading\"></a>"
description: "NetPyNE docs: tutorial.md の日本語訳"
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
<p>原典: <a href="http://doc.netpyne.org/tutorial.html" target="_blank" rel="noopener noreferrer">http://doc.netpyne.org/tutorial.html</a></p>
<p>ライセンス: MIT License for NetPyNE repository documentation/code。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<div class="document" role="main" itemscope="itemscope" itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="netpyne-tutorial" class="section">

<span id="tutorial"></span>

# NetPyNE チュートリアル<a href="#netpyne-tutorial" class="headerlink" title="Link to this heading"></a>

このチュートリアルでは、NetPyNE Python パッケージを使用してニューロン ネットワークの簡単なシミュレーションを作成する方法の概要を説明します。

NetPyNE のダウンロードとインストール手順は、<a href="install.html#install" class="reference internal"><span class="std std-ref">installation</span></a> で参照できます。

Python のネストされた辞書とリストはパラメーターの指定に使用されるため、よく理解しておくことをお勧めします。利用可能な優れたオンライン Python コースが多数あります。 <a href="https://www.codecademy.com/catalog/language/python/" class="reference external">CodeAcademy</a> または <a href="https://developers.google.com/edu/python/" class="reference external">Google</a> から。

<div class="admonition seealso">

こちらも参照

NetPyNE で使用できるすべての機能の包括的な説明については、<a href="user_documentation.html#package-reference" class="reference internal"><span class="std std-ref">ユーザー ドキュメント</span></a> を参照してください。

</div>

<div id="tutorial-1-quick-and-easy-example" class="section">

<span id="simple-example"></span>

## チュートリアル 1: 簡単な例<a href="#tutorial-1-quick-and-easy-example" class="headerlink" title="Link to this heading"></a>

勇気を与える方法で始めるために、わずか 3 行で構成される可能な限り単純な例を実装します。これにより、単純なネットワーク (ランダムに接続された 200 個のセル) が作成され、1 秒間のシミュレーションが実行され、ネットワーク スパイク ラスター プロットとセルの電圧トレースがプロットされます。

<span class="pre">`HHTut.py`</span> サンプル パラメータ ファイルを**ダウンロード**する必要があります (<a href="https://raw.githubusercontent.com/suny-downstate-medical-center/netpyne/development/examples/HHTut/src/HHTut.py" class="reference external">ここからダウンロード</a> - 右クリックして、作業している同じフォルダに「名前を付けて保存」します)。

コードは次のようになります (<a href="_downloads/30d18998fe8d32fcbe705864afbeb370/tut1.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut1.py</code></span></a> から入手できます)。

<div class="highlight-default notranslate">

<div class="highlight">

    import HHTut
    from netpyne import sim
    sim.createSimulateAnalyze(netParams = HHTut.netParams, simConfig = HHTut.simConfig)

</div>

</div>

最初の行は、ネットワークおよびシミュレーション パラメーターを含む <span class="pre">`HHTut`</span> モジュールをインポートします。

2 行目は、<span class="pre">`netpyne`</span> パッケージから <span class="pre">`sim`</span> モジュールをインポートします。 <span class="pre">`sim`</span> モジュールは、これらのパラメータに基づいてネットワークを簡単に作成およびシミュレートする機能を提供します。

3 行目は、<span class="pre">`createSimulateAnalyze`</span> 関数を呼び出します。この関数は、ネットワークを作成およびシミュレートし、データを保存してプロットするための標準的なコマンド シーケンスを実行します。次の 2 つの引数が必要です。

- <span class="pre">`netParams`</span> - ネットワークパラメータ（セルのプロパティ、人口、接続性など）を保存するクラス NetParams のオブジェクト

- <span class="pre">`simConfig`</span> - シミュレーション オプション (期間、dt、記録およびプロットのオプションなど) を保存する SimConfig クラスのオブジェクト

この場合、<span class="pre">`HHTut`</span> モジュール (Hodgkin-Huxley ネットワークの例) で指定された事前定義パラメーターのセットを使用しています。 <span class="pre">`HHTut`</span> モジュールには、<span class="pre">`netParams`</span> および <span class="pre">`simConfig`</span> という 2 つの必須オブジェクトが含まれています。

モデルを実行するには、tut1.py スクリプトを実行するだけです。これを行う 1 つの方法は、次のシェル コマンドを実行することです。

<div class="highlight-default notranslate">

<div class="highlight">

    python tut1.py

</div>

</div>

MPI (例: OpenMPI) と MPI サポートを備えた NEURON が正常にインストールされている場合は、次のように入力して、複数のコア/プロセッサを使用してモデルを並行してシミュレートできます。

<div class="highlight-default notranslate">

<div class="highlight">

    mpiexec -n 4 nrniv -python -mpi tut1.py

</div>

</div>

ここで、4 を使用するコアの数に置き換えます。

毎回その長い行を入力するのを避けたい場合は、この単純なシェル スクリプト (<a href="_downloads/f6e42e822d8b633cb58180b082b752ad/runsim" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">runsim</code></span></a>) をダウンロードして、次のように入力するだけです。

<div class="highlight-default notranslate">

<div class="highlight">

    ./runsim 4 tut1.py

</div>

</div>

<div class="admonition note">

注記

スクリプトを使用するには、スクリプトが実行可能になるように権限を変更してください (例: <span class="pre">`chmod`</span>` `<span class="pre">`+x`</span>` `<span class="pre">`runsim`</span>)。

</div>

どの方法を使用する場合でも、ネットワーク内のセルと接続の 2D 表現、ラスター プロット (セル対時間のスパイク)、および単一セルの電圧トレースを取得する必要があります。

<a href="_images/tut1_net.png" class="reference internal image-reference"><img src="_images/tut1_net.png" style="width: 30%;" alt="_images/tut1_net.png" /></a> <a href="_images/tut1_raster.png" class="reference internal image-reference"><img src="_images/tut1_raster.png" style="width: 33%;" alt="_images/tut1_raster.png" /></a> <a href="_images/tut1_traces.png" class="reference internal image-reference"><img src="_images/tut1_traces.png" style="width: 33%;" alt="_images/tut1_traces.png" /></a>

おめでとう！ NEURON で生物学的ニューロン ネットワークを作成し、シミュレートしました。

<div class="admonition note">

注記

一部のシステムでは、表示される数字が空の場合があります。これは、 tut1.py の末尾に次の行を追加することで修正できます: <span class="pre">`import`</span>` `<span class="pre">`pylab;`</span>` `<span class="pre">`pylab.show()`</span> 。いずれの場合も、ラスター プロットと電圧トレースの数値は、<span class="pre">`HHTut_raster.png`</span> および <span class="pre">`HHTut_traces.png`</span> としてディスクに正しく保存されます。

</div>

このチュートリアルの残りの部分では、独自のパラメーターを簡単に指定してカスタム ネットワークとシミュレーションを作成する方法を見ていきます。わかりやすくするために、ネットワーク パラメーター、シミュレーション オプション、および関数の呼び出し (ネットワークの作成、シミュレーション、結果のプロットに必要) はすべて 1 つのファイルに含まれます。より大きなモデルの場合は、モデル仕様パラメータと関数呼び出しを別のファイルに保存することをお勧めします (<a href="https://https://github.com/Neurosim-lab/netpyne/tree/master/examples" class="reference external">例はこちら</a>を参照)。

まず、Python オブジェクトの概要から始めて、すべてのネットワーク パラメーターを定義します。

</div>

<div id="tutorial-2-network-parameters" class="section">

## チュートリアル 2: ネットワーク パラメーター<a href="#tutorial-2-network-parameters" class="headerlink" title="Link to this heading"></a>

<span class="pre">`netParams`</span> オブジェクトには、ネットワークを定義するために必要な情報がすべて含まれています。これは、次の 8 つの順序付けられた辞書で構成されます。

- <span class="pre">`cellParams`</span> - セルのタイプとそれに関連するパラメータ (セルの形状など)

- <span class="pre">`popParams`</span> - ネットワーク内の人口とそのパラメータ

- <span class="pre">`synMechParams`</span> - シナプス機構とそのパラメータ

- <span class="pre">`connParams`</span> - ネットワーク接続ルールとそれに関連するパラメータ。

- <span class="pre">`subConnParams`</span> - ネットワークのセルラー接続ルールとそれに関連するパラメーター。

- <span class="pre">`stimSourceParams`</span> - 刺激源パラメータ。

- <span class="pre">`stimTargetParams`</span> - 刺激源と標的細胞間のマッピング。

- <span class="pre">`rxdParams`</span> - 反応拡散 (RxD) コンポーネントとそのパラメーター。

<a href="_images/netparams.png" class="reference internal image-reference"><img src="_images/netparams.png" class="align-center" style="width: 40%;" alt="_images/netparams.png" /></a>

<span class="pre">`netParams`</span> 構成は、パッケージが内部で実行されるイベントの標準シーケンスと一致しています。

- <span class="pre">`Network`</span> オブジェクトを作成し、<span class="pre">`popParams`</span> に基づいて <span class="pre">`Population`</span> オブジェクトと <span class="pre">`Cell`</span> オブジェクトのセット内に追加します

- <span class="pre">`cellParams`</span> に基づいてセルのプロパティを設定します

- <span class="pre">`connParams`</span> および <span class="pre">`subConnParams`</span> (どのシナプス前セルとシナプス後セルが conn ルール条件に一致するかを確認) に基づいて、<span class="pre">`synMechParams`</span> のシナプス パラメーターを使用して一連の接続を作成します。

- <span class="pre">`stimSourceParams`</span> および <span class="pre">`stimTargetParams`</span> に基づいて細胞に刺激を追加します。

以下の画像は、このプロセスを示しています。

<a href="_images/process.png" class="reference internal image-reference"><img src="_images/process.png" class="align-center" style="width: 50%;" alt="_images/process.png" /></a>

ここで、新しいモデル ファイル (<span class="pre">`tut2.py`</span> と呼びます) を作成し、すべてのネットワーク パラメーターを最初から指定します。ネットワーク パラメーターを保持する構造を作成するには、次のコードを追加します。

<div class="highlight-default notranslate">

<div class="highlight">

    from netpyne import specs, sim

    # Network parameters
    netParams = specs.NetParams()  # object of class NetParams to store the network parameters

</div>

</div>

<div id="cell-types" class="section">

### セルの種類<a href="#cell-types" class="headerlink" title="Link to this heading"></a>

まず、<span class="pre">`cellParams`</span> ディクショナリに項目を追加して、各セル タイプのプロパティを定義する必要があります。各 <span class="pre">`cellParams`</span> 項目には、キー (セル タイプ) と、次のフィールドを含む辞書で構成される値が含まれています。

- <span class="pre">`secs`</span> - セクションのプロパティを含む辞書。幾何学、機構

この例では、<span class="pre">`PYR`</span> という名前の細胞タイプを作成し、両方の母集団で使用します。特定のジオメトリとホジキン・ハクスリー機構 (<span class="pre">`hh`</span>) を備えた <span class="pre">`soma`</span> というラベルの付いたセクションが必要であることを指定します。

<div class="highlight-default notranslate">

<div class="highlight">

    PYRcell = {'secs': {}}
    PYRcell['secs']['soma'] = {'geom': {}, 'mechs': {}}
    PYRcell['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}                           # soma geometry
    PYRcell['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  # soma hh mechanism
    netParams.cellParams['PYR'] = PYRcell

</div>

</div>

セル タイプの定義に使用されるネストされた辞書構造を少し調べてください。パラメータの入力を容易にするために、空の辞書 (<span class="pre">`{}`</span>) と中間辞書 (例: <span class="pre">`PYRcell`</span>) が使用されていることに注意してください。このルールを追加するには、次のような他の同等の方法もあります。

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.cellParams['PYR'] = {
            'secs': {'soma':
                    {'geom': {'diam': 18.8, 'L': 18.8, 'Ra': 123.0},
                    'mechs': {'hh': {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}}}}})

</div>

</div>

</div>

<div id="populations" class="section">

### 人口<a href="#populations" class="headerlink" title="Link to this heading"></a>

次に、<span class="pre">`netParams`</span> の <span class="pre">`popParams`</span> 辞書に項目を追加して、ネットワーク用の母集団を作成する必要があります。各 <span class="pre">`popParams`</span> 項目には、キー (人口ラベル) と、次の人口パラメータを含むディクショナリで構成される値が含まれています (詳細については、<a href="user_documentation.html#pop-params" class="reference internal"><span class="std std-ref">人口パラメータ</span></a> を参照してください)。

- <span class="pre">`cellType`</span> - この集団内のセルに割り当てられた属性/タグ。後で、このタグを持つセルに特定のセル プロパティを設定するために使用できます。

- <span class="pre">`numCells`</span> - この集団内の細胞の数 (細胞密度を使用して指定することもできます)

- <span class="pre">`cellModel`</span> - この集団内のセルに割り当てられる属性またはタグ。後で、このタグを持つセルに特定のセル モデル実装を設定するために使用できます。例えば「HH」 (標準的なホドギン・ハクスリー型細胞モデル) または「Izhi2007b」 (Izhikevich 2007 点ニューロン モデル)。セル モデルはユーザーが定義することも、インポートすることもできます。

まず、<span class="pre">`S`</span> (感覚) および <span class="pre">`M`</span> (運動) とラベル付けされた 2 つの集団を作成し、それぞれ 20 個の細胞を持ち、<span class="pre">`PYR`</span> (錐体) 型で、<span class="pre">`HH`</span> 細胞モデル (標準的なコンパートメント型ホジキン・ハクスリー型細胞) を使用します。

<div class="highlight-default notranslate">

<div class="highlight">

    ## Population parameters
    netParams.popParams['S'] = {'cellType': 'PYR', 'numCells': 20}
    netParams.popParams['M'] = {'cellType': 'PYR', 'numCells': 20}

</div>

</div>

これにより、実行中に NetPyNE に 40 個の <span class="pre">`Cell`</span> オブジェクトを作成するように指示され、各オブジェクトにはその母集団の属性またはタグ (つまり、「cellType」: 「PYR」など) が含まれます。これらのタグは、後でセルのプロパティや接続ルールを定義するために使用できます。

データ構造をよりよく理解するには、<span class="pre">`print(netParams.popParams)`</span> を実行してすべての母集団パラメータを表示するか、<span class="pre">`print(netParams.popParams['M'])`</span> を出力して母集団 'M' のパラメータを表示します。

</div>

<div id="synaptic-mechanisms-parameters" class="section">

### シナプス機構パラメータ<a href="#synaptic-mechanisms-parameters" class="headerlink" title="Link to this heading"></a>

次に、<span class="pre">`synMechParams`</span> 辞書に項目を追加して、少なくとも 1 つのシナプス メカニズムのパラメーターを定義する必要があります。各 <span class="pre">`synMechParams`</span> 項目には、キー (接続ルールで参照するために使用される synMech ラベル) と、次のフィールドを含む辞書で構成される値が含まれています。

- <span class="pre">`mod`</span> - NMODL メカニズム (例: 「ExpSyn」)

- メカニズムパラメータ (<span class="pre">`tau`</span> または <span class="pre">`e`</span> など) - これらは特定の NMODL メカニズムに依存します。

シナプス機構は、接続フェーズ中に必要に応じて細胞に追加されます。各接続ルールは、適切なラベルを参照することによって、どのシナプス メカニズム パラメーターを使用するかを指定します。私たちのネットワークでは、<span class="pre">`Exp2Syn`</span> モデルを使用して実装され、立ち上がり時間 (<span class="pre">`tau1`</span>) が 0.1 ミリ秒、減衰時間 (<span class="pre">`tau2`</span>) が 5 ミリ秒、平衡電位 (<span class="pre">`e`</span>) が 0 である、<span class="pre">`exc`</span> というラベルの付いた単純な興奮性シナプス機構のパラメーターを定義します。 mV:

<div class="highlight-default notranslate">

<div class="highlight">

    ## Synaptic mechanism parameters
    netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 5.0, 'e': 0}  # excitatory synaptic mechanism

</div>

</div>

</div>

<div id="stimulation" class="section">

### 刺激<a href="#stimulation" class="headerlink" title="Link to this heading"></a>

<span class="pre">`NetStim`</span> (NEURON の人工スパイク発生器) を使用して、細胞にバックグラウンド刺激を加えてみましょう。 <span class="pre">`bkg`</span> というラベルの付いた刺激源を作成し、発火速度が <span class="pre">`100`</span> Hz、ノイズ レベルが <span class="pre">`0.5`</span> であることを指定します。

<div class="highlight-default notranslate">

<div class="highlight">

    # Stimulation parameters
    netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5}

</div>

</div>

次に、この刺激の対象となる細胞を指定します。この場合、すべての錐体細胞が必要なので、条件を <span class="pre">`{'cellType':`</span>` `<span class="pre">`'PYR'}`</span> に設定します。最後に、NetStims を重み 0.01、遅延 5 ミリ秒で接続し、<span class="pre">`exc`</span> シナプス メカニズムをターゲットにします。

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.stimTargetParams['bkg->PYR'] = {'source': 'bkg', 'conds': {'cellType': 'PYR'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}

</div>

</div>

</div>

<div id="connectivity-rules" class="section">

### 接続ルール<a href="#connectivity-rules" class="headerlink" title="Link to this heading"></a>

最後に、<span class="pre">`connParams`</span> ディクショナリに項目 (接続ルール) を追加して、セルを接続する方法を指定する必要があります。各 <span class="pre">`connParams`</span> 項目には、キー (conn ルール ラベル) と、次のフィールドを含むディクショナリで構成される値が含まれています。

- <span class="pre">`preConds`</span> - シナプス前細胞の状態を指定します

- <span class="pre">`postConds`</span> - シナプス後細胞の状態を指定します

- <span class="pre">`weight`</span> - 接続のシナプス強度

- <span class="pre">`delay`</span> - シナプス前スパイクがシナプス後ニューロンに到達するまでの遅延 (ミリ秒)

- <span class="pre">`synMech`</span> - 使用するシンパティックメカニズムパラメータ

- <span class="pre">`probability`</span> または <span class="pre">`convergence`</span> または <span class="pre">`divergence`</span> - 接続の確率 (0 ～ 1)、収束 (ポストシン セルあたりのプレシン セルの数)、または発散 (プレシン セルあたりのポストシン セルの数) の確率をそれぞれ指定するオプションのパラメーター。省略した場合、全対全接続が実装されます。

50% の確率で感覚集団と運動集団をランダムに結び付けるルールを追加します。

<div class="highlight-default notranslate">

<div class="highlight">

    ## Cell connectivity rules
    netParams.connParams['S->M'] = { #  S -> M label
            'preConds': {'pop': 'S'},   # conditions of presyn cells
            'postConds': {'pop': 'M'},  # conditions of postsyn cells
            'probability': 0.5,         # probability of connection
            'weight': 0.01,             # synaptic weight
            'delay': 5,                 # transmission delay (ms)
            'synMech': 'exc'}           # synaptic mechanism

</div>

</div>

</div>

<div id="simulation-configuration-options" class="section">

### シミュレーション構成オプション<a href="#simulation-configuration-options" class="headerlink" title="Link to this heading"></a>

上記で、ネットワーク モデルに関連するすべてのパラメーターを定義しました。ここでは、ネットワークから独立したシミュレーション自体のパラメータまたは構成 (期間など) を指定します。

<span class="pre">`simConfig`</span> オブジェクトを使用して、シミュレーション期間、タイムステップ、セル変数の記録、ディスクへのデータの保存、グラフのプロットなどに関連するオプションをカスタマイズできます。すべてのオプションにはデフォルト値があるため、それらを指定することは必須ではありません。

以下に、0.025 ミリ秒の積分ステップで 1 秒のシミュレーションを実行し、0.1 ミリ秒間隔でソーマ電圧を記録し、<span class="pre">`model_output`</span> という名前の pickle ファイルにデータ (パラメーター、ネットワーク、およびシミュレーション出力) を保存し、ネットワーク ラスターをプロットし、gid <span class="pre">`1`</span> でセルの電圧トレースをプロットし、ネットワークの 2D 表現をプロットするために必要なオプションを示します。

<div class="highlight-default notranslate">

<div class="highlight">

    # Simulation options
    simConfig = specs.SimConfig()       # object of class SimConfig to store simulation configuration

    simConfig.duration = 1*1e3          # Duration of the simulation, in ms
    simConfig.dt = 0.025                # Internal integration timestep to use
    simConfig.verbose = False           # Show detailed messages
    simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
    simConfig.recordStep = 0.1          # Step size in ms to save data (e.g. V traces, LFP, etc)
    simConfig.filename = 'tut2'         # Set file output name
    simConfig.savePickle = False        # Save params, network and sim output to pickle file

    simConfig.analysis['plotRaster'] = {'saveFig': True}                  # Plot a raster
    simConfig.analysis['plotTraces'] = {'include': [1], 'saveFig': True}  # Plot recorded traces for this list of cells
    simConfig.analysis['plot2Dnet'] = {'saveFig': True}                   # plot 2D cell positions and connections

</div>

</div>

シミュレーション構成オプションの完全なリストは、<a href="user_documentation.html#sim-config" class="reference internal"><span class="std std-ref">シミュレーション構成</span></a>から入手できます。

</div>

<div id="network-creation-and-simulation" class="section">

### ネットワークの作成とシミュレーション<a href="#network-creation-and-simulation" class="headerlink" title="Link to this heading"></a>

すべてのネットワーク パラメーターとシミュレーション オプションを定義したので、実際にネットワークを作成してシミュレーションを実行する準備が整いました。これを行うには、<span class="pre">`sim`</span> モジュールの <span class="pre">`createSimulateAnalyze`</span> 関数を使用し、作成したばかりの <span class="pre">`netParams`</span> 辞書と <span class="pre">`simConfig`</span> 辞書を引数として渡します。

<div class="highlight-default notranslate">

<div class="highlight">

    sim.createSimulateAnalyze(netParams, simConfig)

</div>

</div>

前と同様に、<span class="pre">`sim`</span> モジュールを <span class="pre">`netpyne`</span> パッケージからインポートしたことを確認する必要があることに注意してください。

この例の完全なチュートリアル コードは、ここから入手できます: <a href="_downloads/b1cf60be43bf73795e03ca52b97dcbc6/tut2.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut2.py</code></span></a>

モデルを実行するには、<a href="#simple-example" class="reference internal"><span class="std std-ref">チュートリアル 1: 簡単な例</span></a> で前述したいずれかの方法を使用できます。

mpi がインストールされていない場合:

<div class="highlight-default notranslate">

<div class="highlight">

    python tut2.py

</div>

</div>

mpi が動作している場合:

<div class="highlight-default notranslate">

<div class="highlight">

    mpiexec -n 4 nrniv -python -mpi tut2.py

</div>

</div>

mpi が動作しており、<span class="pre">`runsim`</span> シェル スクリプトがある場合:

<div class="highlight-default notranslate">

<div class="highlight">

    ./runsim 4 tut2.py

</div>

</div>

以下に示すラスター プロットと電圧トレースの図が得られるはずです。 <span class="pre">`M`</span> 母集団の発火率が <span class="pre">`S`</span> 母集団の発火率よりも高いことに注目してください。両方とも同じバックグラウンド入力を受信するため、これは理にかなっていますが、<span class="pre">`S`</span> セルは <span class="pre">`M`</span> セルにランダムに接続するため、<span class="pre">`M`</span> の起動レートが増加します。

<a href="_images/tut2_net.png" class="reference internal image-reference"><img src="_images/tut2_net.png" style="width: 30%;" alt="_images/tut2_net.png" /></a> <a href="_images/tut2_raster.png" class="reference internal image-reference"><img src="_images/tut2_raster.png" style="width: 33%;" alt="_images/tut2_raster.png" /></a> <a href="_images/tut2_traces.png" class="reference internal image-reference"><img src="_images/tut2_traces.png" style="width: 33%;" alt="_images/tut2_traces.png" /></a>

モデルパラメータを変更した場合の効果を自由に調べてください。細胞の数、バックグラウンドまたはS-\>Mの重み、細胞の形状または生物物理学的特性など。

</div>

</div>

<div id="tutorial-3-adding-a-compartment-dendrite-to-cells" class="section">

## チュートリアル 3: セルにコンパートメント (樹状突起) を追加する<a href="#tutorial-3-adding-a-compartment-dendrite-to-cells" class="headerlink" title="Link to this heading"></a>

ここでは、受動機構を備えた樹状セクションを追加することで錐体細胞タイプを拡張します。 <span class="pre">`dend`</span> セクションには、親の <span class="pre">`soma`</span> セクションへの接続方法を定義する <span class="pre">`topol`</span> dict が含まれていることに注意してください。

<div class="highlight-default notranslate">

<div class="highlight">

    ## Cell types
    PYRcell = {'secs': {}}

    PYRcell['secs']['soma'] = {'geom': {}, 'mechs': {}}
    PYRcell['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}
    PYRcell['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}

    PYRcell['secs']['dend'] = {'geom': {}, 'topol': {}, 'mechs': {}}
    PYRcell['secs']['dend']['geom'] = {'diam': 5.0, 'L': 150.0, 'Ra': 150.0, 'cm': 1}
    PYRcell['secs']['dend']['topol'] = {'parentSec': 'soma', 'parentX': 1.0, 'childX': 0}
    PYRcell['secs']['dend']['mechs']['pas'] = {'g': 0.0000357, 'e': -70}

    netParams.cellParams['PYR'] = PYRcell

</div>

</div>

次のように dict エントリ <span class="pre">`'sec':`</span>` `<span class="pre">`'dend'`</span> を追加することで、接続ルールを更新して、<span class="pre">`S`</span> セルが <span class="pre">`M`</span> セルの樹状突起に接続するように指定することもできます。

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.connParams['S->M'] = {  #  S -> M
            'preConds': {'pop': 'S'},     # presynaptic conditions
            'postConds': {'pop': 'M'},    # postsynaptic conditions
            'probability': 0.5,           # probability of connection
            'weight': 0.01,               # synaptic weight
            'delay': 5,                   # transmission delay (ms)
            'sec': 'dend',                # section to connect to
            'loc': 1.0,                   # location of synapse
            'synMech': 'exc'}             # target synaptic mechanism

</div>

</div>

この例の完全なチュートリアル コードは、<a href="_downloads/400786a8cf76ad952c08614cf65cb3fb/tut3.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut3.py</code></span></a> から入手できます。

ネットワークを実行すると、新しい樹状コンパートメントが発火率を低下させる効果があることが観察されます。

</div>

<div id="tutorial-4-using-a-simplified-cell-model-izhikevich" class="section">

## チュートリアル 4: 単純化されたセル モデルの使用 (Izhikevich)<a href="#tutorial-4-using-a-simplified-cell-model-izhikevich" class="headerlink" title="Link to this heading"></a>

大規模なシミュレーションを扱う場合、速度を上げるために、一部の集団に対してより単純なセル モデルを使用すると便利な場合があります。ここでは、感覚 (<span class="pre">`S`</span>) 集団内の細胞のみを対象として、HH モデルをより単純な Izhikevich 細胞モデルに置き換えます。

最初のステップは、Izhi2007b ポイント プロセス メカニズムを含む Izhikevich セル NEURON NMODL ファイルをダウンロードすることです: <a href="_downloads/803a7312bae028b7a24ba7f3e28de705/izhi2007b.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">izhi2007b.mod</code></span></a>

次に、この .mod ファイルをコンパイルして、NEURON で使用できるようにする必要があります。チュートリアルと MOD ファイルをダウンロードしたディレクトリに移動し、次のコマンドを実行します。

<div class="highlight-default notranslate">

<div class="highlight">

    nrnivmodl

</div>

</div>

次に、HH セル タイプの名前を変更し、Izhikevich セル用の新しいセル タイプを作成します。

<div class="highlight-default notranslate">

<div class="highlight">

    ## Cell types
    PYR_HH = {'secs': {}}
    PYR_HH['secs']['soma'] = {'geom': {}, 'mechs': {}}                                                    # soma params dict
    PYR_HH['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}                               # soma geometry
    PYR_HH['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}      # soma hh mechanisms
    PYR_HH['secs']['dend'] = {'geom': {}, 'topol': {}, 'mechs': {}}                                       # dend params dict
    PYR_HH['secs']['dend']['geom'] = {'diam': 5.0, 'L': 150.0, 'Ra': 150.0, 'cm': 1}                      # dend geometry
    PYR_HH['secs']['dend']['topol'] = {'parentSec': 'soma', 'parentX': 1.0, 'childX': 0}                  # dend topology
    PYR_HH['secs']['dend']['mechs']['pas'] = {'g': 0.0000357, 'e': -70}                                   # dend mechanisms
    netParams.cellParams['PYR_HH'] = PYR_HH                                                               # add dict to list of cell parameters

    PYR_Izhi = {'secs': {}}
    PYR_Izhi['secs']['soma'] = {'geom': {}, 'pointps': {}}                        # soma params dict
    PYR_Izhi['secs']['soma']['geom'] = {'diam': 10.0, 'L': 10.0, 'cm': 31.831}    # soma geometry
    PYR_Izhi['secs']['soma']['pointps']['Izhi'] = {                               # soma Izhikevich properties
            'mod':'Izhi2007b',
            'C':1,
            'k':0.7,
            'vr':-60,
            'vt':-40,
            'vpeak':35,
            'a':0.03,
            'b':-2,
            'c':-50,
            'd':100,
            'celltype':1}
    netParams.cellParams['PYR_Izhi'] = PYR_Izhi                                   # add dict to list of cell parameters

</div>

</div>

<span class="pre">`soma`</span> 内に <span class="pre">`pointps`</span> という新しいフィールドが追加されていることに注目してください。このフィールドには、このセクションのポイント プロセス メカニズムが含まれます。この場合、<span class="pre">`Izhi2007b`</span> ポイント プロセスを追加し、ピラミッド型の規則的なスパイク セルに対応する Izhikevich セル パラメーターを含む辞書を提供しました。 Izhikevich セル モデルの詳細とその他のパラメーターは、<a href="https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=39948" class="reference external">こちらでご覧いただけます。</a>

次に、<span class="pre">`S`</span> 母集団に対して <span class="pre">`PYR_Izhi`</span> <span class="pre">`cellType`</span> を使用することを指定する必要があります。

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.popParams['S'] = {'cellType': 'PYR_Izhi', 'numCells': 20}
    netParams.popParams['M'] = {'cellType': 'PYR_HH', 'numCells': 20}

</div>

</div>

おめでとうございます。これで、HH セルと Izhikevich セルで構成されるハイブリッド モデルが完成しました。既存または新規の集団で使用される細胞モデルを簡単に変更することもできます。

この例の完全なチュートリアル コードは、<a href="_downloads/1dad775bc8818b50767f723adc07d58c/tut4.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut4.py</code></span></a> から入手できます。

<div class="admonition seealso">

こちらも参照

NetPyNE は、他のファイル (hoc セル テンプレートや Python クラスなど) で定義されたセルのインポートもサポートしています。詳細と例については、<a href="user_documentation.html#importing-cells" class="reference internal"><span class="std std-ref">外部定義セル モデルのインポート</span></a>を参照してください。

</div>

</div>

<div id="tutorial-5-position-and-distance-based-connectivity" class="section">

## チュートリアル 5: 位置および距離ベースの接続<a href="#tutorial-5-position-and-distance-based-connectivity" class="headerlink" title="Link to this heading"></a>

次の例は、集団を空間的に分離し、抑制集団を追加し、セルの位置または距離に依存する重み、接続確率、および遅延を実装する方法を示します。

2/3、4、5 の 3 つの層に分散された 6 つの集団 (3 つの興奮性と 3 つの抑制性) を持つ皮質のようなネットワークを構築します。<span class="pre">`tut5.py`</span> という新しい空のファイルを作成し、必要なコードを追加しましょう。

セルを空間的に分散させたいので、最初に行う必要があるのは、セルが配置されるボリュームの寸法を定義することです。慣例により、X と Z は水平方向または横方向の寸法、Y は垂直方向の寸法 (この場合は皮質の深さを表す) とみなされます。体積が 100x1000x100 um (つまり、水平方向の広がりが 100x100 um、皮質の深さが 1000um) の直方体を定義するには、次のように <span class="pre">`sizeX`</span>、<span class="pre">`sizeY`</span>、および <span class="pre">`sizeZ`</span> ネットワーク パラメーターを使用できます。

<div class="highlight-default notranslate">

<div class="highlight">

    # Network parameters
    netParams = specs.NetParams()     # object of class NetParams to store the network parameters

    netParams.sizeX = 100             # x-dimension (horizontal length) size in um
    netParams.sizeY = 1000            # y-dimension (vertical height or cortical depth) size in um
    netParams.sizeZ = 100             # z-dimension (horizontal length) size in um
    netParams.propVelocity = 100.0    # propagation velocity (um/ms)
    netParams.probLengthConst = 150.0 # length constant for conn probability (um)

</div>

</div>

2 つのパラメーター (<span class="pre">`propVelocity`</span> と <span class="pre">`probLengthConst`</span>) も追加したことに注意してください。これらは後で接続ルールに使用します。

次に、各タイプの細胞の細胞特性を定義します (「E」は興奮性、「I」は抑制性)。異なるセルタイプが異なるプロパティを持つ可能性があることを示すために、いくつかのセルパラメータにランダムな小さな変更を加えました。

<div class="highlight-default notranslate">

<div class="highlight">

    ## Cell types
    secs = {} # sections dict
    secs['soma'] = {'geom': {}, 'mechs': {}}                                                # soma params dict
    secs['soma']['geom'] = {'diam': 15, 'L': 14, 'Ra': 120.0}                               # soma geometry
    secs['soma']['mechs']['hh'] = {'gnabar': 0.13, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  # soma hh mechanism
    netParams.cellParams['E'] = {'secs': secs}                                              # add dict to list of cell params

    secs = {} # sections dict
    secs['soma'] = {'geom': {}, 'mechs': {}}                                                # soma params dict
    secs['soma']['geom'] = {'diam': 10.0, 'L': 9.0, 'Ra': 110.0}                            # soma geometry
    secs['soma']['mechs']['hh'] = {'gnabar': 0.11, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  # soma hh mechanism
    netParams.cellParams['I'] = {'secs': secs}                                              # add dict to list of cell params

</div>

</div>

次に、バックグラウンド入力集団と、細胞の種類と層に従ってラベル付けされた 6 つの皮質集団を作成できます。層 2 の興奮性細胞の「E2」。<span class="pre">`yRange`</span> パラメーターを使用して、各集団の皮質深さの範囲を定義できます。レイヤー 2 セルを 100 ～ 300 um の深さに配置するには: <span class="pre">`'yRange':`</span>` `<span class="pre">`[100,300]`</span>。この範囲は、正規化された値を使用して指定することもできます。 <span class="pre">`'yRange':`</span>` `<span class="pre">`[0.1,0.3]`</span>。以下のコードでは、説明のために両方のメソッドの例を示しています。

<div class="highlight-default notranslate">

<div class="highlight">

    ## Population parameters
    netParams.popParams['E2'] = {'cellType': 'E', 'numCells': 50, 'yRange': [100,300]}
    netParams.popParams['I2'] = {'cellType': 'I', 'numCells': 50, 'yRange': [100,300]}
    netParams.popParams['E4'] = {'cellType': 'E', 'numCells': 50, 'yRange': [300,600]}
    netParams.popParams['I4'] = {'cellType': 'I', 'numCells': 50, 'yRange': [300,600]}
    netParams.popParams['E5'] = {'cellType': 'E', 'numCells': 50, 'ynormRange': [0.6,1.0]}
    netParams.popParams['I5'] = {'cellType': 'I', 'numCells': 50, 'ynormRange': [0.6,1.0]}

</div>

</div>

前の例と同様に、興奮性および抑制性のシナプス機構のパラメーターも追加します。これらは、接続の作成時にセルに追加されます。

<div class="highlight-default notranslate">

<div class="highlight">

    ## Synaptic mechanism parameters
    netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.8, 'tau2': 5.3, 'e': 0}  # NMDA synaptic mechanism
    netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}  # GABA synaptic mechanism

</div>

</div>

刺激に関しては、ネットワーク内のすべてのセルにバックグラウンド入力を追加します。重みは 0.01 に固定されますが、平均 5 ミリ秒、標準偏差 2 のガウス分布から遅延を取得し、最小値を 1 ミリ秒にします。これは、文字列ベースの関数 <span class="pre">`'max(1,`</span>` `<span class="pre">`normal(5,2)'`</span> を使用して行うことができます。 <a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a> セクションで詳しく説明されているように、文字列ベースの関数を使用すると、多くの Python 数学演算子と関数を使用して接続パラメーターを定義できます。バックグラウンド刺激を追加する完全なコードは次のようになります。

<div class="highlight-default notranslate">

<div class="highlight">

    # Stimulation parameters
    netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 20, 'noise': 0.3}
    netParams.stimTargetParams['bkg->all'] = {'source': 'bkg', 'conds': {'cellType': ['E','I']}, 'weight': 0.01, 'delay': 'max(1, normal(5,2))', 'synMech': 'exc'}

</div>

</div>

これで、標準のシミュレーション構成オプションと、ネットワークを作成して実行するためのコードを追加できるようになりました。各興奮性集団の 1 つの細胞の電圧トレースを記録してプロットすることを選択したことに注目してください。 (<span class="pre">`{'include':`</span>` `<span class="pre">`[('E2',0),`</span>` `<span class="pre">`('E4',`</span>` `<span class="pre">`0),`</span>` `<span class="pre">`('E5',`</span>` `<span class="pre">`5)]})`</span>)、細胞の皮質深さに基づいて順序付けされたラスター (<span class="pre">`{'orderBy':`</span>` `<span class="pre">`'y',`</span>` `<span class="pre">`'orderInverse':`</span>Q` `<span class="pre">`True})`</span>) をプロットし、細胞の位置と接続の 2D 視覚化を表示し、接続性マトリックスをプロットします。

<div class="highlight-default notranslate">

<div class="highlight">

    # Simulation options
    simConfig = specs.SimConfig()        # object of class SimConfig to store simulation configuration

    simConfig.duration = 1*1e3           # Duration of the simulation, in ms
    simConfig.dt = 0.05                  # Internal integration timestep to use
    simConfig.verbose = False            # Show detailed messages
    simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
    simConfig.recordStep = 1             # Step size in ms to save data (e.g. V traces, LFP, etc)
    simConfig.filename = 'tut5'          # Set file output name
    simConfig.savePickle = False         # Save params, network and sim output to pickle file

    simConfig.analysis['plotRaster'] = {'orderBy': 'y', 'orderInverse': True, 'saveFig': True}         # Plot a raster
    simConfig.analysis['plotTraces'] = {'include': [('E2',0), ('E4', 0), ('E5', 5)], 'saveFig': True}  # Plot recorded traces for this list of cells
    simConfig.analysis['plot2Dnet'] = {'saveFig': True}                                                # plot 2D cell positions and connections
    simConfig.analysis['plotConn'] = {'saveFig': True}                                                 # plot connectivity matrix

    # Create network and run simulation
    sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)

</div>

</div>

この時点でモデルを実行すると、指定どおりにセルが 3 つのレイヤーに分散されており、バックグラウンド入力によって駆動される平均レート 20 Hz ですべてランダムにスパイクしていることがわかります。

<a href="_images/tut5_conn_1.png" class="reference internal image-reference"><img src="_images/tut5_conn_1.png" style="width: 17%;" alt="_images/tut5_conn_1.png" /></a> <a href="_images/tut5_net_1.png" class="reference internal image-reference"><img src="_images/tut5_net_1.png" style="width: 17%;" alt="_images/tut5_net_1.png" /></a> <a href="_images/tut5_raster_1.png" class="reference internal image-reference"><img src="_images/tut5_raster_1.png" style="width: 35%;" alt="_images/tut5_raster_1.png" /></a> <a href="_images/tut5_traces_1.png" class="reference internal image-reference"><img src="_images/tut5_traces_1.png" style="width: 30%;" alt="_images/tut5_traces_1.png" /></a>

次に、NetPyNE の機能を説明するために、いくつかの空間依存プロパティを持つ興奮的な接続を追加してみましょう。まず、コード <span class="pre">`'postConds':`</span>` `<span class="pre">`{'y':`</span>` `<span class="pre">`[100,1000]}`</span> を使用して、興奮性細胞が皮質深さ 100 および 1000 um 内のすべての細胞をターゲットにするように指定しましょう。

次に、接続の重みを細胞の皮質の深さに比例させましょう。つまり、より深い層のシナプス後細胞は、表層の細胞よりも強い接続を受けます。これを行うために、NetPyNE が文字列ベースの関数で使用できるようにする距離関連の変数を利用します。この場合、<span class="pre">`post_ynorm`</span> は、シナプス後細胞の正規化された y 位置を表します。使用可能な変数の完全なリストについては、<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照してください。

最後に、<span class="pre">`'delay':`</span>` `<span class="pre">`'dist_3D/propVelocity'`</span> のように、セル間の距離 (<span class="pre">`dist_3D`</span>) と伝播速度 (コードの先頭にパラメーターとして指定) に基づいて遅延を指定できます。この接続ルールの完全なコードは次のとおりです。

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.connParams['E->all'] = {
      'preConds': {'cellType': 'E'}, 'postConds': {'y': [100,1000]},  #  E -> all (100-1000 um)
      'probability': 0.1 ,                  # probability of connection
      'weight': '0.005*post_ynorm',         # synaptic weight
      'delay': 'dist_3D/propVelocity',      # transmission delay (ms)
      'synMech': 'exc'}                     # synaptic mechanism

</div>

</div>

モデルを実行すると、興奮性の接続が赤で表示され、脱分極の遮断につながる重みの増加により、より深い層 (y 値が高い) の細胞がより低いレートとより高い同期を示す様子が示されます。この違いは、レイヤー 2 セルとレイヤー 5 セルの電圧トレースにも見られます。

<a href="_images/tut5_conn_2.png" class="reference internal image-reference"><img src="_images/tut5_conn_2.png" style="width: 17%;" alt="_images/tut5_conn_2.png" /></a> <a href="_images/tut5_net_2.png" class="reference internal image-reference"><img src="_images/tut5_net_2.png" style="width: 17%;" alt="_images/tut5_net_2.png" /></a> <a href="_images/tut5_raster_2.png" class="reference internal image-reference"><img src="_images/tut5_raster_2.png" style="width: 35%;" alt="_images/tut5_raster_2.png" /></a> <a href="_images/tut5_traces_2.png" class="reference internal image-reference"><img src="_images/tut5_traces_2.png" style="width: 30%;" alt="_images/tut5_traces_2.png" /></a>

最後に、説明の目的で、ここでは <span class="pre">`pop`</span> 属性を使用して指定された、興奮性細胞にのみ投影される抑制性の接続を追加します (同等のルールは、<span class="pre">`'postConds':`</span>` `<span class="pre">`{'cellType':`</span>` `<span class="pre">`'E'}`</span> になります)。

接続の確率を、指定された長さの定数 (<span class="pre">`probLengthConst`</span>) で距離の関数として指数関数的に減衰させるには、距離ベースの式 <span class="pre">`'probability':`</span>` `<span class="pre">`'0.4*exp(-dist_3D/probLengthConst)'`</span> を使用できます。したがって、抑制的な接続ルールのコードは次のようになります。

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.connParams['I->E'] = {                          # I -> E
            'preConds': {'cellType': 'I'},                        # presynaptic conditions
            'postConds': {'pop': ['E2','E4','E5']},               # postsynaptic conditions
            'probability': '0.4*exp(-dist_3D/probLengthConst)',   # probability of connection
            'weight': 0.001,                                      # synaptic weight
            'delay': 'dist_3D/propVelocity',                      # transmission delay (ms)
            'synMech': 'inh'}                                     # synaptic mechanism

</div>

</div>

2D ネットワーク図では、抑制性の接続が青色で表示されており、距離に関連する確率の制限により、これらはほとんどが層内のローカル/ラテラルにあることに注意してください。これらの局所的な抑制的な接続により全体の同期性が低下し、ネットワークの一時的な発火パターンに豊かさが導入されます。

<a href="_images/tut5_conn_3.png" class="reference internal image-reference"><img src="_images/tut5_conn_3.png" style="width: 17%;" alt="_images/tut5_conn_3.png" /></a> <a href="_images/tut5_net_3.png" class="reference internal image-reference"><img src="_images/tut5_net_3.png" style="width: 17%;" alt="_images/tut5_net_3.png" /></a> <a href="_images/tut5_raster_3.png" class="reference internal image-reference"><img src="_images/tut5_raster_3.png" style="width: 35%;" alt="_images/tut5_raster_3.png" /></a> <a href="_images/tut5_traces_3.png" class="reference internal image-reference"><img src="_images/tut5_traces_3.png" style="width: 30%;" alt="_images/tut5_traces_3.png" /></a>

この例の完全なチュートリアル コードは、<a href="_downloads/710f744a66a23d1e5b32313a7fae0110/tut5.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut5.py</code></span></a> から入手できます。

</div>

<div id="tutorial-6-adding-stimulation-to-the-network" class="section">

## チュートリアル 6: ネットワークに刺激を追加する<a href="#tutorial-6-adding-stimulation-to-the-network" class="headerlink" title="Link to this heading"></a>

細胞刺激パラメータを指定するために 2 つの辞書構造が使用されます。<span class="pre">`stimSourceParams`</span> は刺激源のパラメータを定義します。および <span class="pre">`stimTargetParams`</span> は、どのセルにどのような刺激源を適用するかを指定します (ソースのセルへのマッピング)。詳細については、<a href="user_documentation.html#stimulation" class="reference internal"><span class="std std-ref">刺激パラメータ</span></a>を参照してください。

この例では、<a href="_downloads/b1cf60be43bf73795e03ca52b97dcbc6/tut2.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut2.py</code></span></a> の単純なネットワークを開始点として使用し、すべての接続パラメーターを削除し、代わりに外部刺激を追加します。

以下に、それぞれ異なるタイプの 4 つの典型的な NEURON 刺激源 (IClamp、VClamp、AlphaSynapse、NetStim) を追加します。パラメーター値には、たとえばオンセット値の均一な分布 (<span class="pre">`'onset':`</span>` `<span class="pre">`'uniform(600,800)'`</span>) や、ターゲット セルの正規化された深さ (<span class="pre">`'gmax':`</span>` `<span class="pre">`'post_ynorm'`</span>):

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.stimSourceParams['Input_1'] = {'type': 'IClamp', 'del': 300, 'dur': 100, 'amp': 'uniform(0.4,0.5)'}
    netParams.stimSourceParams['Input_2'] = {'type': 'VClamp', 'dur': [0,50,200], 'amp': [-60,-30,40], 'gain': 1e5, 'rstim': 1, 'tau1': 0.1, 'tau2': 0}
    netParams.stimSourceParams['Input_3'] = {'type': 'AlphaSynapse', 'onset': 'uniform(300,600)', 'tau': 5, 'gmax': 'post_ynorm', 'e': 0}
    netParams.stimSourceParams['Input_4'] = {'type': 'NetStim', 'interval': 'uniform(20,100)', 'number': 1000, 'start': 600, 'noise': 0.1}

</div>

</div>

<span class="pre">`stimTargetParams`</span> dict に項目を追加することで、上記の刺激源のいずれかをネットワーク内のセルのサブセットにマッピングまたは適用できるようになりました。任意のセルタグ (「pop」、「cellType」、または「ynorm」など) を使用して、どのセルを刺激するかを選択できることに注意してください。さらに、「cellList」オプションを使用すると、選択したセルのサブセット（例：「S」集団の最初の 15 個のセル）内のセルの特定のリスト（相対セル ID を使用）をターゲットにすることができます。

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.stimTargetParams['Input_1->S'] = {'source': 'Input_1', 'sec':'soma', 'loc': 0.8, 'conds': {'pop':'S', 'cellList': range(15)}}
    netParams.stimTargetParams['Input_2->S'] = {'source': 'Input_2', 'sec':'soma', 'loc': 0.5, 'conds': {'pop':'S', 'ynorm': [0,0.5]}}
    netParams.stimTargetParams['Input_3->M1'] = {'source': 'Input_3', 'sec':'soma', 'loc': 0.2, 'conds': {'pop':'M', 'cellList': [2,4,5,8,10,15,19]}}
    netParams.stimTargetParams['Input_4->PYR'] = {'source': 'Input_4', 'sec':'soma', 'loc': 0.5, 'weight': '0.1+normal(0.2,0.05)','delay': 1, 'conds': {'cellType':'PYR', 'ynorm': [0.6,1.0]}}

</div>

</div>

<div class="admonition note">

注記

NetStim を各ターゲット セルにマッピング/適用するために新しい接続が作成されるため、NetStims の stimTargetParams には接続パラメータ (重みや遅延など) が必要です。

</div>

<div class="admonition note">

注記

NetStims は、上記の方法 (刺激として) を使用するか、<span class="pre">`'cellModel':`</span>` `<span class="pre">`'NetStim'`</span> で母集団を作成して適切な接続を追加することによって追加できます。

</div>

さまざまなタイプの刺激を使用して上記のネットワークを実行すると、次のラスターが生成されるはずです。

<a href="_images/tut6_raster.png" class="reference internal image-reference"><img src="_images/tut6_raster.png" class="align-center" style="width: 50%;" alt="_images/tut6_raster.png" /></a>

この例の完全なチュートリアル コードは、<a href="_downloads/7d3385ecb5fbf72ce83901a916327123/tut6.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut6.py</code></span></a> から入手できます。

</div>

<div id="tutorial-7-modifying-the-instantiated-network-interactively" class="section">

## チュートリアル 7: インスタンス化されたネットワークを対話的に変更する<a href="#tutorial-7-modifying-the-instantiated-network-interactively" class="headerlink" title="Link to this heading"></a>

この例は、ネットワーク モデルと NEURON オブジェクトを含む NetPyNE で生成された構造を直接操作したいと考えている経験豊富なユーザーを対象としています。セルが全対全に接続され、相互抑制により発火が同期するホップフィールド-ブロディ ネットワークをモデル化します (他のセルからの抑制によりリセットが提供され、セルが一緒にロックされます)。同期のレベルは、対話的に変更する接続の重みによって異なります。

まず、50 個のセルからなる 1 つの母集団 (<span class="pre">`hop`</span>) と 50 Hz のバックグラウンド入力を持つ単純なネットワークを記述する新しいファイル (<span class="pre">`tut7.py`</span>) を作成します (前の簡単なチュートリアルの例 <span class="pre">`tut2.py`</span> と同様)。 <span class="pre">`hop`</span> 母集団内に全対全抑制結合を作成しますが、最初は重みを 0 に設定します。

<div class="highlight-default notranslate">

<div class="highlight">

    from netpyne import specs

    ###############################################################################
    # NETWORK PARAMETERS
    ###############################################################################

    netParams = specs.NetParams()  # object of class NetParams to store the network parameters

    # Cell parameters
    ## PYR cell properties
    secs = {}
    secs['soma'] = {'geom': {}, 'topol': {}, 'mechs': {}}
    secs['soma']['geom'] = {'diam': 18.8, 'L': 18.8}
    secs['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}
    netParams.cellParams['PYR'] = {'secs': secs}  # add dict to list of cell properties

    # Population parameters
    netParams.popParams['hop'] = {'cellType': 'PYR', 'cellModel': 'HH', 'numCells': 50}      # add dict with params for this pop
    #netParams.popParams['background'] = {'cellModel': 'NetStim', 'rate': 50, 'noise': 0.5}  # background inputs

    # Synaptic mechanism parameters
    netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 1.0, 'e': 0}
    netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 1.0, 'e': -80}

    # Stimulation parameters
    netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 50, 'noise': 0.5}
    netParams.stimTargetParams['bkg->all'] = {'source': 'bkg', 'conds': {'pop': 'hop'}, 'weight': 0.1, 'delay': 1, 'synMech': 'exc'}

    # Connectivity parameters
    netParams.connParams['hop->hop'] = {
            'preConds': {'pop': 'hop'},         # presynaptic conditions
            'postConds': {'pop': 'hop'},        # postsynaptic conditions
            'weight': 0.0,                      # weight of each connection
            'synMech': 'inh',                   # target inh synapse
            'delay': 5}                         # delay

</div>

</div>

ここで、標準のシミュレーション構成オプションを追加し、<span class="pre">`syncLines`</span> オプションを含めて、ラスター プロットに同期性を示す各スパイクで垂直線が表示されるようにします。

<div class="highlight-default notranslate">

<div class="highlight">

    ###############################################################################
    # SIMULATION PARAMETERS
    ###############################################################################
    simConfig = specs.SimConfig()  # object of class SimConfig to store simulation configuration

    # Simulation options
    simConfig.duration = 0.5*1e3        # Duration of the simulation, in ms
    simConfig.dt = 0.025                # Internal integration timestep to use
    simConfig.verbose = False           # Show detailed messages
    simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
    simConfig.recordStep = 1            # Step size in ms to save data (eg. V traces, LFP, etc)
    simConfig.filename = 'model_output' # Set file output name
    simConfig.savePickle = False        # Save params, network and sim output to pickle file

    simConfig.analysis['plotRaster'] = {'syncLines': True, 'saveFig': True}      # Plot a raster
    simConfig.analysis['plotTraces'] = {'include': [1], 'saveFig': True}         # Plot recorded traces for this list of cells
    simConfig.analysis['plot2Dnet'] = {'saveFig': True}                          # plot 2D cell positions and connections

</div>

</div>

最後に、ネットワークを作成してシミュレーションを実行するコードを追加しますが、説明のために、プロセスの各ステップで個別の関数呼び出しを使用します (前に使用した包括的な <span class="pre">`sim.createAndSimulate()`</span> 関数の代わりに)。

<div class="highlight-default notranslate">

<div class="highlight">

    ###############################################################################
    # EXECUTION CODE (via netpyne)
    ###############################################################################
    from netpyne import sim

    # Create network and run simulation
    sim.initialize(                     # create network object and set cfg and net params
            simConfig = simConfig,          # pass simulation config and network params as arguments
            netParams = netParams)
    sim.net.createPops()                # instantiate network populations
    sim.net.createCells()               # instantiate network cells based on defined populations
    sim.net.connectCells()              # create connections between cells based on params
    sim.net.addStims()                  # add stimulation
    sim.setupRecording()                # setup variables to record for each cell (spikes, V traces, etc)
    sim.runSim()                        # run parallel Neuron simulation
    sim.gatherData()                    # gather spiking data and cell info from each node
    sim.saveData()                      # save params, cell info and sim output to file (pickle,mat,txt,etc)
    sim.analysis.plotData()             # plot spike raster

</div>

</div>

上記のコードを実行すると、結果として得られるネットワーク 2D マップには抑制的な接続が青色で表示されますが、重みが 0 であるため、これらはまだ何の影響もありません。ラスター プロットは、50 Hz のバックグラウンド入力によって駆動されるランダムな発火と、0.26 の低い同期測定を示しています (赤い垂直線は同期性の悪さを示しています)。

<a href="_images/tut7_net_1.png" class="reference internal image-reference"><img src="_images/tut7_net_1.png" style="width: 30%;" alt="_images/tut7_net_1.png" /></a> <a href="_images/tut7_raster_1.png" class="reference internal image-reference"><img src="_images/tut7_raster_1.png" style="width: 33%;" alt="_images/tut7_raster_1.png" /></a> <a href="_images/tut7_traces_1.png" class="reference internal image-reference"><img src="_images/tut7_traces_1.png" style="width: 32%;" alt="_images/tut7_traces_1.png" /></a>

<div class="admonition note">

注記

これで、すべてのセルと接続のメタデータ、および関連する NEURON オブジェクト (セクション、ネットコンなど) を含むインスタンス化されたネットワークにアクセスできるようになります。 <span class="pre">`sim`</span> オブジェクトには <span class="pre">`net`</span> オブジェクトが含まれており、このオブジェクトには <span class="pre">`cells`</span> という Cell オブジェクトのリストが含まれています。各 Cell オブジェクトには、タグ (<span class="pre">`tags`</span>)、セクション (<span class="pre">`secs`</span>)、接続 (<span class="pre">`conns`</span>)、および外部入力 (<span class="pre">`stims`</span>) を含む構造が含まれています。 NEURON オブジェクトは、この Python 階層構造内に含まれています。詳細については、<a href="user_documentation.html#data-model" class="reference internal"><span class="std std-ref">NetPyNE データ モデル (インスタンス化されたネットワークと出力データの構造)</span></a> を参照してください。

</div>

<div class="admonition note">

注記

人口オブジェクトのリストは <span class="pre">`sim.net.pops`</span> から入手できます。各オブジェクトには、この集団に属するセルのすべての gid を含むリスト <span class="pre">`cellGids`</span> と、集団プロパティを含む辞書 <span class="pre">`tags`</span> が含まれます。

</div>

<div class="admonition note">

注記

スパイク データは <span class="pre">`sim.allSimData['spkt']`</span> および <span class="pre">`sim.allSimData['spkid']`</span> 経由で入手できます。電圧トレースは、例えば次の方法で入手できます。 <span class="pre">`sim.allSimData['V']['cell_25']`</span> (gid 25 のセルの場合)。

</div>

<div class="admonition note">

注記

すべてのシミュレーション構成オプションは、<span class="pre">`sim.cfg`</span> を介して対話的に変更できます。たとえば、2D 視覚化のプロットをオフにするには、次を実行します: <span class="pre">`sim.cfg.analysis['plot2Dnet']=False`</span>

</div>

NetPyNE によって生成されたインスタンス化されたネットワーク構造の表現を以下に示します。

<a href="_images/netstruct.png" class="reference internal image-reference"><img src="_images/netstruct.png" class="align-center" style="width: 80%;" alt="_images/netstruct.png" /></a>

ネットワーク オブジェクト <span class="pre">`net`</span> は、セル、接続、および刺激パラメータを簡単に変更する機能も提供します:それぞれ <span class="pre">`modifyCells(params)`</span>、<span class="pre">`modifyConns(params)`</span>、および <span class="pre">`modifyStims(params)`</span>。 <span class="pre">`params`</span> 引数の構文は、最初にネットワーク パラメータを設定するために使用される構文、つまり、設定する条件とパラメータを含む辞書に似ています。詳細については、<a href="user_documentation.html#network-methods" class="reference internal"><span class="std std-ref">ネットワーク クラス メソッド</span></a> を参照してください。

したがって、<span class="pre">`sim.net.modifyConns()`</span> 関数を呼び出して、抑制性接続のすべての重みを (たとえば 0.5 に) 増加させてから、対話的にシミュレーションを再実行できます。

<div class="highlight-default notranslate">

<div class="highlight">

    ###############################################################################
    # INTERACTING WITH INSTANTIATED NETWORK
    ###############################################################################

    # modify conn weights
    sim.net.modifyConns({'conds': {'label': 'hop->hop'}, 'weight': 0.5})

    sim.runSim()                          # run parallel Neuron simulation
    sim.gatherData()                      # gather spiking data and cell info from each node
    sim.saveData()                        # save params, cell info and sim output to file (pickle,mat,txt,etc)
    sim.analysis.plotData()               # plot spike raster

</div>

</div>

<div class="admonition note">

注記

この条件では、以前に作成された再帰接続のセットを参照する hop-\>hop ラベルを使用しました。

</div>

結果のプロットは、相互抑制の増加によりネットワーク アクティビティが同期し、同期測定値が 0.69 に増加することを示しています。

<a href="_images/tut7_raster_2.png" class="reference internal image-reference"><img src="_images/tut7_raster_2.png" style="width: 33%;" alt="_images/tut7_raster_2.png" /></a> <a href="_images/tut7_traces_2.png" class="reference internal image-reference"><img src="_images/tut7_traces_2.png" style="width: 32%;" alt="_images/tut7_traces_2.png" /></a>

さらに、セルのプロパティの一部を変更して、これが同期性にどのような影響を与えるかを観察することもできます。以下のコードは、「ホップ」集団内のすべての細胞の細胞体長を 160 um に変更します。

<div class="highlight-default notranslate">

<div class="highlight">

    # modify cells geometry
    sim.net.modifyCells({'conds': {'pop': 'hop'},
                        'secs': {'soma': {'geom': {'L': 160}}}})

    sim.simulate()
    sim.analysis.plotRaster(syncLines=True)
    sim.analysis.plotTraces(include = [1])

</div>

</div>

<div class="admonition note">

注記

説明のために、単純に <span class="pre">`runSim()`</span> および <span class="pre">`gatherData()`</span> を呼び出す <span class="pre">`sim.simulate()`</span> ラッパーを使用します。さらに、<span class="pre">`sim.plotRaster()`</span> 関数と <span class="pre">`sim.plotTraces()`</span> 関数を対話的に呼び出します。

</div>

結果のプロットは、新しいセル形状による発火率の低下と同期性の増加を示しています。

<a href="_images/tut7_raster_3.png" class="reference internal image-reference"><img src="_images/tut7_raster_3.png" style="width: 33%;" alt="_images/tut7_raster_3.png" /></a> <a href="_images/tut7_traces_3.png" class="reference internal image-reference"><img src="_images/tut7_traces_3.png" style="width: 32%;" alt="_images/tut7_traces_3.png" /></a>

この例の完全なチュートリアル コードは、<a href="_downloads/b3a5b6807b959fdb313482a4c0d99362/tut7.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut7.py</code></span></a> から入手できます。

</div>

<div id="tutorial-8-running-batch-simulations" class="section">

## チュートリアル 8: バッチ シミュレーションの実行<a href="#tutorial-8-running-batch-simulations" class="headerlink" title="Link to this heading"></a>

ここでは、チュートリアル 2 の単純なネットワークを使用してバッチ シミュレーションを実行する方法を説明します。バッチ シミュレーションとは、特定の範囲内でいくつかのパラメーター値を変更し、これらのパラメーター値のすべての組み合わせに対してシミュレーションを自動的に実行することを意味します (グリッド パラメーター検索とも呼ばれます)。

最初に行う必要があるのは、tut2.py コードを 3 つの異なるファイルに分割することです。このような小さなモデルには必要ありませんが、これはより大規模で複雑なモデルには非常に役立ちます。ファイル構成は次のようになります (ダウンロードするにはファイル名をクリックします)。

- <a href="_downloads/5810ef33ffc308cf6c38dbb7dde1bd46/tut8_netParams.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut8_netParams.py</code></span></a> : ネットワーク モデル (netParams オブジェクト) を定義します。セル、シナプス、接続、刺激などの「固定」パラメータ値が含まれます。このファイルへの変更は、モデルを比較的安定して改善する場合にのみ行う必要があります。モデルの探索または調整のために体系的に変更されるパラメーター値は、シミュレーション構成 (cfg) モジュールの適切な変数を参照することによってここに含める必要があります。シミュレーションの各バッチに必要な netParams ファイルは 1 つだけです。

- <a href="_downloads/002a13ee17217bbeb58cf3a067d6e50b/tut8_cfg.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut8_cfg.py</code></span></a> : シミュレーション構成 (simConfig オブジェクト)。期間、dt、記録パラメータなどの各シミュレーション実行のパラメータ値が含まれます。また、ネットワークの探索または調整のために変更されるモデル パラメータも含まれます。バッチを実行すると、NetPyNE はパラメータ設定ごとに 1 つの cfg ファイルを自動的に作成します (これを開始点として使用します)。

- <a href="_downloads/51401b525803a9e987834f98e9639507/tut8_init.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut8_init.py</code></span></a> : 単一シミュレーションを実行するコマンドのシーケンス。 「python init.py」経由で実行できます。バッチを実行するとき、NetPyNE は init.py を複数回呼び出し、調査されたパラメータ設定ごとに異なる cfg ファイルを渡します。

バッチ シミュレーションを制御するために新しいファイルを追加する必要もあります。

- <a href="_downloads/30dbf256475b46e9ec70a0cfbb5505f4/tut8_batch.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut8_batch.py</code></span></a> : シミュレーションのバッチで調査されるパラメーターとパラメーター値、実行構成 (MPI+Bulletin Board を使用するかどうかなど) を定義します。マルチコア マシン) または SLURM/PBS Torque (HPC 用))、およびバッチを実行するコマンド。

要約すると、**netParams.py** は固定 (ネットワーク) パラメーター、**cfg.py** は可変 (シミュレーション) パラメーター、**init.py** はシミュレーションを実行し、**batch.py​​* はパラメーター値の組み合わせを調べるシミュレーションのバッチを実行します。

接続の重みとシナプスの減衰時定数がモーター集団の発火率にどのように影響するかを調査したいとします。最初のステップは、これらのパラメーターが可変になるように、つまりシミュレーションごとに異なるように <span class="pre">`tut8_netParams.py`</span> を変更することです。したがって、これらを固定値 (例: 5.0 や 0.01) から simConfig の変数に依存するように変更します: <span class="pre">`cfg.synMechTau2`</span> および <span class="pre">`cfg.connWeight`</span> (簡単にするために <span class="pre">`simConfig`</span> の名前を <span class="pre">`cfg`</span> に変更したことに注意してください)。

<div class="highlight-default notranslate">

<div class="highlight">

    ...

    ## Synaptic mechanism parameters
    netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': cfg.synMechTau2, 'e': 0}  # excitatory synaptic mechanism

    ...

    ## Cell connectivity rules
    netParams.connParams['S->M'] = {    #  S -> M label
            'preConds': {'pop': 'S'},       # conditions of presyn cells
            'postConds': {'pop': 'M'},      # conditions of postsyn cells
            'probability': 0.5,             # probability of connection
            'weight': cfg.connWeight,       # synaptic weight
            'delay': 5,                     # transmission delay (ms)
            'synMech': 'exc'}               # synaptic mechanism

</div>

</div>

したがって、これら 2 つの変数が使用できるように、<span class="pre">`tut8_netParams.py`</span> を変更して <span class="pre">`cfg`</span> モジュールをインポートする必要もあります。コードはまず <span class="pre">`__main__`</span> から <span class="pre">`cfg`</span> モジュールをロードしようとします。これは、ユーザーが最初に実行した親モジュール (この場合は <span class="pre">`tut8_init.py`</span>) を指します。前に述べたように、<span class="pre">`tut8_init.py`</span> は <span class="pre">`netParams`</span> と <span class="pre">`cfg`</span> の両方をロードし、シミュレーションを実行します。これが失敗した場合、コードは <span class="pre">`cfg`</span> ファイルから <span class="pre">`cfg`</span> を直接ロードします。これを実装するには、<span class="pre">`tut8_netParams.py`</span> の先頭に次の行を追加します。

<div class="highlight-default notranslate">

<div class="highlight">

    try:
            from __main__ import cfg  # import SimConfig object with params from parent module
    except:
            from tut8_cfg import cfg  # if no simConfig in parent module, import directly from tut8_cfg module

</div>

</div>

次のステップでは、これら 2 つの変数を <span class="pre">`tut8_cfg.py`</span> に追加して、それらが存在し、netParams によって使用され、バッチ シミュレーションで変更できるようにします。

<div class="highlight-default notranslate">

<div class="highlight">

    # Variable parameters (used in netParams)
    cfg.synMechTau2 = 50
    cfg.connWeight = 0.01

</div>

</div>

また、各母集団の平均発火率が画面に表示され、出力ファイルに保存されるように、次の行を <span class="pre">`tut8_cfg.py`</span> に追加することに注意してください。

<div class="highlight-default notranslate">

<div class="highlight">

    cfg.printPopAvgRates = True

</div>

</div>

<span class="pre">`tut8_init.py`</span> には、<span class="pre">`tut2.py`</span> と比較して 3 行のみが含まれ、新しい行は 1 行だけ含まれます。この新しい行は、コマンド ラインからの引数の読み取りを処理するメソッド <span class="pre">`readCmdLineArgs`</span> を呼び出します。 NetPyNE は、異なるパラメーターの組み合わせで複数の cfg ファイルを作成し、次の形式のコマンド ライン引数を使用して実行するため、これはバッチ シミュレーションを実行するために必要です。これは NetPyNE によってバックグラウンドで行われるため、心配する必要はありません。 <span class="pre">`tut8_init.py`</span> は次のようになります。

<div class="highlight-default notranslate">

<div class="highlight">

    from netpyne import sim

    # read cfg and netParams from command line arguments if available; otherwise use default
    simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='tut8_cfg.py', netParamsDefault='tut8_netParams.py')

    # Create network and run simulation
    sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)

</div>

</div>

この時点で、たとえば次のコマンドを使用してシミュレーションを実行できます。 <span class="pre">`python`</span>` `<span class="pre">`tut8_init.py`</span> とすると、チュートリアル 2 (<span class="pre">`tut2.py`</span>) と同じ結果が生成されるはずです。

次に、バッチ シミュレーションに関連するすべての情報を含む <span class="pre">`tut8_batch.py`</span> を追加します。この特定のパラメーターの組み合わせを調べるために、関数 <span class="pre">`batchTauWeight`</span> を定義しました。後で他の同様の関数を定義して、他のバッチを作成することもできます。

最初に行うことは、順序付き辞書 <span class="pre">`params`</span> を作成することです。これは特別な NetPyNE タイプ (<span class="pre">`specs.ODict`</span>) になりますが、基本的には順序付き辞書のように動作します。次に、この辞書のキーとして探索するパラメーター (<span class="pre">`synMechTau2`</span> および <span class="pre">`connWeight`</span>) を追加し、バッチ シミュレーションで試すパラメーター値のリストを辞書キーとして追加します (<span class="pre">`[3.0,`</span>` `<span class="pre">`5.0,`</span>` `<span class="pre">`7.0]`</span>)。 <span class="pre">`[0.005,`</span>` `<span class="pre">`0.01,`</span>` `<span class="pre">`0.15]`</span>。パラメータ名は、<span class="pre">`cfg`</span> で定義された変数と一致する必要があることに注意してください。

次に、NetPyNE クラス <span class="pre">`Batch`</span> のオブジェクト <span class="pre">`b`</span> を作成し、探索するパラメータと、netParams および simConfig モジュールを含むファイルを引数として渡します。最後に、出力ファイルの作成に使用されるバッチ ラベル (<span class="pre">`'tauWeight'`</span>) など、<span class="pre">`Batch`</span> オブジェクトのいくつかの属性をカスタマイズします。データを保存するフォルダー (<span class="pre">`'tut8_data'`</span>)、パラメーターの探索に使用されるメソッド (<span class="pre">`'grid'`</span>)、つまりパラメーター値のすべての組み合わせ。そして、<span class="pre">`'mpi'`</span> (これは MPI と NEURON の掲示板を使用します。スーパーコンピューターには他のオプションが利用可能です) を使用することを示す実行構成、各 SIM を実行するための <span class="pre">`'tut8_init.py'`</span>、および出力ファイルが既に存在する場合は <span class="pre">`'skip'`</span> が実行されます。

最後に、バッチ シミュレーションを起動するコマンド <span class="pre">`b.run()`</span> を追加するだけです。

<span class="pre">`tut8_batch.py`</span> は次のようになります。

<div class="highlight-default notranslate">

<div class="highlight">

    from netpyne import specs
    from netpyne.batch import Batch

    def batchTauWeight():
            # Create variable of type ordered dictionary (NetPyNE's customized version)
            params = specs.ODict()

            # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
            params['synMechTau2'] = [3.0, 5.0, 7.0]
            params['connWeight'] = [0.005, 0.01, 0.15]

            # create Batch object with parameters to modify, and specifying files to use
            b = Batch(params=params, cfgFile='tut8_cfg.py', netParamsFile='tut8_netParams.py',)

            # Set output folder, grid method (all param combinations), and run configuration
            b.batchLabel = 'tauWeight'
            b.saveFolder = 'tut8_data'
            b.method = 'grid'
            b.runCfg = {'type': 'mpi',
                                    'script': 'tut8_init.py',
                                    'skip': True}

            # Run batch simulations
            b.run()

    # Main code
    if __name__ == '__main__':
            batchTauWeight()

</div>

</div>

バッチ シミュレーションを実行するには、MPI が適切にインストールされ、MPI を使用するように NEURON が設定されている必要があります。次のコマンドを実行します。 <span class="pre">`mpiexec`</span>` `<span class="pre">`-np`</span>` `<span class="pre">`[num_cores]`</span>` `<span class="pre">`nrniv`</span>` `<span class="pre">`-python`</span>` `<span class="pre">`-mpi`</span>` `<span class="pre">`tut8_batch.py`</span>ここで、<span class="pre">`[num_cores]`</span> は、使用するプロセッサの数に置き換える必要があります。ジョブ (マスター ノード) をスケジュールするために使用されるため、最低限必要な値は <span class="pre">`2`</span> です。例えば4 つのプロセッサを選択した場合、1 つはジョブのスケジュールに使用され、他の 3 つは異なるパラメータの組み合わせで NEURON シミュレーションを実行します。

シミュレーションが完了すると、次のファイルを含む新しいフォルダー <span class="pre">`tut8_data`</span> が作成されます。

- **tauWeight_netParams.py**: 使用される元の netParams ファイルのコピー (<span class="pre">`tut8_netParams.py`</span>)

- **tauWeight_batchScript.py**: 使用された元のバッチ ファイルのコピー (<span class="pre">`tut8_batch.py`</span>)

- **tauWeight_batch.json**: バッチ パラメーターと使用される実行オプションを含む JSON ファイル。

- パラメーターの組み合わせごとに (x、y はパラメーター値のインデックスを表します):

> <div>
  >
  > - **tauWeight_x_y_cfg.json**: <span class="pre">`tut8_cfg.py`</span> からコピーされたすべての <span class="pre">`cfg`</span> 変数を含む JSON ファイルですが、バッチ パラメーターのこの特定の組み合わせの <span class="pre">`synMechTau2`</span> および <span class="pre">`connWeight`</span> の値が含まれています。
  >
  > - **tauWeight_x_y.json**: このバッチ パラメーターの組み合わせの出力データを含む JSON ファイル。出力データには、デフォルトで <span class="pre">`netParams`</span>、<span class="pre">`net`</span>、<span class="pre">`simConfig`</span>、および <span class="pre">`simData`</span> が含まれます。
  >
  > - **tauWeight_x_y_raster.png** および **tauWeight_x_y_traces.png**: このパラメーターの組み合わせの数値を出力します。
  >
  > </div>

出力データを分析するには、<a href="_downloads/6ecdb5b7d499ed217ca64fe5b228e291/tut8_analysis.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut8_analysis.py</code></span></a> をダウンロードできます。このファイルには、バッチ シミュレーションの結果を示す行列を読み取ってプロットする関数が含まれています。このファイルには、<a href="http://pandas.pydata.org/" class="reference external">Pandas</a> および <a href="https://seaborn.pydata.org/" class="reference external">Seaborn</a> パッケージが必要です。

<div class="admonition note">

注記

(<span class="pre">`tut8_analysis.py`</span>) の分析関数はすぐに NetPyNE に統合される予定なので、コードの詳細については説明しません。

</div>

<span class="pre">`python`</span>` `<span class="pre">`tut8_analysis.py`</span> を実行すると、調べた 2 つのパラメーターと <span class="pre">`M`</span> 母集団の発火率との関係を示すカラー プロットが生成されます。

<a href="_images/tut8_analysis.png" class="reference internal image-reference"><img src="_images/tut8_analysis.png" style="width: 50%;" alt="_images/tut8_analysis.png" /></a>

最初は接続重みの関数としてレートが増加しますが、その後、脱分極の遮断によりレートが減少することに注目してください。そして、シナプス時間減衰定数（synMechTau2）の影響が、細胞が正常にスパイクしているか遮断されているかにどのように依存するか。バッチ シミュレーションと分析により、これらの複雑な相互作用の探索と理解が容易になります。

<div class="admonition note">

注記

より上級のユーザーのために、バッチを実行するときに NetPyNE が内部で行うことは次のとおりです。

1. netParams.py (または指定されたファイル) をバッチ データ フォルダーにコピーします。

2. cfg.py (または指定されたファイル) から cfg (SimConfig オブジェクト) をロードします。

3. パラメータの組み合わせを繰り返します。

    > <div>
    >
    > 3a) Modify cfg (SimConfig object) with the parameter values
    >
    > 3b) Save cfg to .json file
    >
    > 3c) Run simulation by passing netParams.py and cfg.json files as arguments; this means the code in netParams.py is executed each time but cfg is just a set of fixed saved values.
    >
    > </div>

</div>

<div class="admonition seealso">

こちらも参照

Batch クラスで使用できるオプションの完全な説明は、間もなく <a href="user_documentation.html#package-reference" class="reference internal"><span class="std std-ref">ユーザー ドキュメント</span></a> で公開される予定です。

</div>

</div>

<div id="tutorial-9-recording-and-plotting-lfps" class="section">

## チュートリアル 9: LFP の記録とプロット<a href="#tutorial-9-recording-and-plotting-lfps" class="headerlink" title="Link to this heading"></a>

単一セルおよびネットワークの局所電場電位 (LFP) を記録および分析する方法の例は、サンプル フォルダー <a href="https://github.com/suny-downstate-medical-center/netpyne/tree/master/examples/LFPrecording" class="reference external">LFP 記録サンプル </a> に含まれています。 LFP 記録は並列シミュレーションでも機能します。

LFP を記録するには、simConfig 属性の RecordLFP に LFP 電極の 3D 位置のリストを設定するだけです。 <span class="pre">`simConfig.recordLFP`</span>` `<span class="pre">`=`</span>` `<span class="pre">`e.g.`</span>` `<span class="pre">`[[50,`</span>` `<span class="pre">`100,`</span>` `<span class="pre">`50],`</span>` `<span class="pre">`[50,`</span>` `<span class="pre">`200,`</span>` `<span class="pre">`50]]`</span> (y 座標は深さを表すため、プロットすると負の値として表されることに注意してください)。各電極の LFP 信号は、各ニューロンの各セグメントによって寄与される細胞外電位を合計することによって得られます。細胞外電位は、「線源近似」を使用し、導電率シグマ = 0.3 mS/mm のオーミック媒体を仮定して計算されます。 LFP のモデリングの詳細については、<a href="http://www.scholarpedia.org/article/Local_field_potential" class="reference external">Scholarpedia</a> または <a href="https://doi.org/10.3389/fncom.2016.00065" class="reference external">この記事</a> を参照してください。

記録された LFP 信号は、サイズ timeSteps \* numElectrodes の 2D リストとして <span class="pre">`sim.allSimData['LFP']`</span> に保存されます。 sim.allSimData\['LFP'\]\[10\]\[2\]\` corresponds to the LFP value of electrode 2 at time step 10. It is possible to record the LFP signal generated by each individual cell by setting <span class="pre">`simConfig.saveLFPCells`</span>` `<span class="pre">`=`</span>` `<span class="pre">`True`</span> – this will be stored in <span class="pre">`sim.allSimData['LFPCells']`</span> をサイズ セル \* timeSteps \* numElectrodes の 3D リストとして表現します。

LFP をプロットするには、<span class="pre">`sim.analysis.plotLFP()`</span> メソッドを使用します。これにより、各電極について、1) 時間分解 LFP 信号 (「timeSeries」)、2) パワースペクトル密度 (「PSD」)、3) スペクトログラム / 時間周波数プロファイル (「スペクトログラム」)、4) およびモデルニューロン上に重ねられた電極の 3D 位置 (「位置」) をプロットすることができます。 <span class="pre">`plotLFP()`</span> 引数の完全なリストについては、<a href="user_documentation.html#analysis-functions" class="reference internal"><span class="std std-ref">分析関連関数</span></a> を参照してください。

<a href="https://github.com/suny-downstate-medical-center/netpyne/tree/master/examples/LFPrecording/src/cell" class="reference external">最初の例</a> は、700 以上のコンパートメント (セグメント) と複数の体細胞および樹状イオン チャネルを持つ単一細胞 (M1 皮質脊髄ニューロン) の LFP 記録を示しています。セルのパラメーターは .json ファイルからロードされます。細胞は、興奮性シナプスを介して細胞体に NetStim 入力を受け取ります。 10 個の LFP 電極がニューロンの両側の 5 つの異なる皮質深さに配置されます。細胞体電圧、LFP 時間分解信号、および電極の 3D 位置がプロットされます。

<a href="_images/lfp_cell.png" class="reference internal image-reference"><img src="_images/lfp_cell.png" class="align-center" style="width: 60%;" alt="_images/lfp_cell.png" /></a>

<a href="https://github.com/suny-downstate-medical-center/netpyne/tree/master/examples/LFPrecording/src/net" class="reference external">2 番目の例</a> は、チュートリアル 5 で示したものと非常によく似たネットワークの LFP 記録を示しています。ただし、この場合、細胞はより現実的なモデル、つまり複数のイオン チャネルを持つ 6 コンパートメントの M1 皮質線条体ニューロンに置き換えられています。セルのパラメーターは .json ファイルからロードされます。細胞は NetStim 入力を受け取り、興奮性および抑制性の接続を含みます。 4 つの LFP 電極が異なる皮質深さに配置されます。ラスター プロットと LFP 時間分解信号、PSD、スペクトログラム、および電極の 3D 位置がプロットされます。

<a href="_images/lfp_net.png" class="reference internal image-reference"><img src="_images/lfp_net.png" class="align-center" style="width: 90%;" alt="_images/lfp_net.png" /></a>

</div>

<div id="tutorial-10-network-with-reaction-diffusion-rxd" class="section">

## チュートリアル 10: 反応拡散を使用したネットワーク (RxD)<a href="#tutorial-10-network-with-reaction-diffusion-rxd" class="headerlink" title="Link to this heading"></a>

NetPyNE の高レベル仕様は、<a href="https://www.neuron.yale.edu/neuron/static/docs/rxd/index.html" class="reference external">NEURON の反応拡散 (RxD)</a> コンポーネントもサポートしています。 RxD を使用すると、分子 (カルシウム、カリウム、IP3 など) の細胞内、細胞内 (小胞体やミトコンドリアなどの細胞小器官を含む)、細胞外での拡散 (代謝、リン酸化、緩衝、セカンド メッセンジャー カスケードなど) のシグナル伝達と酵素処理の状況を指定できます。これは、分子レベルの化学生理学を、細胞内、細胞、およびネットワークスケールでの古典的な電気生理学に結び付けるのに役立ちます。

<span class="pre">`netParams.rxdParams`</span> 辞書を使用して、さまざまな RxD コンポーネント (<span class="pre">`regions`</span>、<span class="pre">`species`</span>、<span class="pre">`states`</span>、<span class="pre">`reactions`</span>、<span class="pre">`multicompartmentReactions`</span>、および <span class="pre">`rates`</span>) を定義できます。単一セルおよびネットワーク内の RxD コンポーネントを含むサンプル モデルは、サンプル フォルダーに含まれています: <a href="https://github.com/Neurosim-lab/netpyne/tree/development/examples/rxd_buffering" class="reference external">RxD バッファリング example</a> および <a href="https://github.com/Neurosim-lab/netpyne/tree/development/examples/rxd_net" class="reference external">RxD ネットワーク example</a>。 RxD は並列シミュレーションでも動作します。

<div class="admonition seealso">

こちらも参照

NetPyNE で使用できるすべての機能の包括的な説明については、<a href="user_documentation.html#package-reference" class="reference internal"><span class="std std-ref">ユーザー ドキュメント</span></a> を参照してください。

</div>

</div>

</div>

</div>

</div>
</section>

</article>
</main>
