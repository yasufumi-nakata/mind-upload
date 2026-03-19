# Site Deepening Audit (2026-03-19, Datasets Inverse-Benchmark Board)

## 対象

- 主対象: `datasets.md`

## 今回の選定理由

- 2026-03-19 時点で公開サイトは、`external validation` を `stimulation ground truth`、`simultaneous invasive recording`、`postsurgical outcome` に分けるところまでは進んでおりました。
- しかし実践導線である `datasets.md` には、なお `C-stage data を使った = solver comparison の公平な土台が整った` と読める余地が残っておりました。
- これは技術・自然科学の観点で重要です。なぜなら、EEG inverse problem では `validation class` を固定しただけでは足りず、`source regime (focal / sparse / extended)`、`same geometry / same preprocessing`、`conductivity and hyperparameter sensitivity`、`inter-method disagreement` を分けて書かなければ、`solver X won` が簡単に過大読みに変わるからです。

## 根拠付き批判

### 1. 旧 `datasets.md` は validation class を分けても、solver benchmark governance がまだ弱すぎました

- 問題:
  - 旧ページは stage C の中で `stimulation`、`simultaneous SEEG`、`postsurgical outcome` を分けておりました。
  - しかし、同じ C-stage data を使っても `same raw data / same head model / same electrode coordinates / same source space / same conductivity sweep` を固定しなければ、公平な solver comparison にはなりませんでした。
- 根拠:
  - Michel & Brunet (2019) は ESI を単一アルゴリズムではなく multi-step pipeline として整理しました。
  - Unnwongse et al. (2023) は localization error が source depth と skull conductivity に依存することを human intracranial stimulation で示しました。
  - Aydin et al. (2019) は conductivity uncertainty 自体が dipole reconstruction を動かすことを示しました。
- 批判:
  - したがって `validated dataset` を持っていることと `fair solver board` を持っていることは別です。
  - 旧実践ページは前者をかなり整理していた一方、後者の公開規律がまだ不足しておりました。

### 2. 旧ページは `focal-source benchmark` と `extended-source benchmark` を十分に分けていませんでした

- 問題:
  - stage C の説明では direct validation の重要性は書かれていましたが、`which source class the benchmark actually favors` が不十分でした。
- 根拠:
  - Pascarella et al. (2023) は in-vivo focal-source benchmark で ten methods を比較し、dipolar / sparsity-promoting methods が distributed methods より低い localization error を示しうる一方、parameter sensitivity が method ごとに大きく異なると示しました。
  - Feng et al. (2025) は Block-Champagne を extended-source reconstruction 用として提案し、simulation と DBS / epilepsy data で extended source の位置と extent の同時再構成を評価しました。
- 批判:
  - よって `focal-source board で勝った method` をそのまま `extended-source reconstruction` の一般 winner にしてはいけません。
  - 旧ページではこの source-regime split が明示されておらず、読者が `one leaderboard` を想像しやすい構造でした。

### 3. 旧ページは inter-method disagreement の stop rule をまだ要求していませんでした

- 問題:
  - `MNE / beamformer / Champagne` のような family が乖離したとき、旧ページは `どの条件で順位が入れ替わったか` を開示する運用まで固定していませんでした。
- 根拠:
  - Pascarella et al. (2023) は best localization error だけでなく regularization sensitivity と montage-density effect が method ごとに異なることを示しました。
  - Baillet et al. (2001) は phantom 実験で head model と regularization scheme が結果に大きく効くことを示しました。
  - Cai et al. (2021) と Phillips et al. (2005) は empirical-Bayesian / Champagne 系で noise estimation や prior handling が reconstruction を変えることを示しました。
- 批判:
  - したがって 1 回勝った run だけを出して `solver X is better` と書くのは弱すぎます。
  - 必要なのは、`rank stability across sensitivity sweeps` と `family disagreement summary` を public artifact に含めることでした。

## 今回実行した変更

- `datasets.md`
  - `last_updated` を `2026-03-19` に更新しました。
  - front matter に inverse-problem benchmark governance を反映し、`solver family / source regime / sensitivity report` を page highlights と known points に追加しました。
  - validation ladder の直後に新規節 `4.5) Inverse-problem benchmark board: compare error questions, not solver names` を追加しました。
  - benchmark question ごとに
    - focal-source localization
    - simultaneous invasive concordance
    - postsurgical / clinical concordance
    - extended-source / multimodal-prior reconstruction
    を分け、何を固定し、何を metric とし、何を過大読みにしてはいけないかを table 化しました。
  - `If MNE / beamformer / Champagne disagree` table を追加し、conductivity / geometry / regularization / source-depth / source-regime による順位反転時の safe reading を固定しました。
  - checklist に `Inverse-problem governance` を追加し、実践ページでも leaderboard 主張より disclosure を先に要求するようにしました。
  - 参考文献に Baillet (2001), Phillips (2005), Michel & Brunet (2019), Aydin (2019), Cai (2021), Pascarella (2023), Feng (2025) を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文と監査メモの更新で完結しております。

## 参考文献

1. Baillet S, Riera JJ, Marin G, et al. Evaluation of inverse methods and head models for EEG source localization using a human skull phantom. *Physics in Medicine and Biology*. 2001;46(1):77-96.
   - https://doi.org/10.1088/0031-9155/46/1/306
2. Phillips C, Mattout J, Rugg MD, Maquet P, Friston KJ. An empirical Bayesian solution to the source reconstruction problem in EEG. *NeuroImage*. 2005;24(4):997-1011.
   - https://doi.org/10.1016/j.neuroimage.2004.10.030
3. Michel CM, Brunet D. EEG source imaging: a practical review of the analysis steps. *Frontiers in Neurology*. 2019;10:325.
   - https://doi.org/10.3389/fneur.2019.00325
4. Aydin U, Vorwerk J, Kupper P, et al. Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. *Frontiers in Neuroscience*. 2019;13:531.
   - https://doi.org/10.3389/fnins.2019.00531
5. Cai C, Sekihara K, Nagarajan SS. Robust estimation of noise for electromagnetic brain imaging with the Champagne algorithm. *NeuroImage*. 2021;225:117411.
   - https://doi.org/10.1016/j.neuroimage.2020.117411
6. Pascarella A, Mikulan E, Sciacchitano F, et al. An in-vivo validation of ESI methods with focal sources. *NeuroImage*. 2023;277:120219.
   - https://doi.org/10.1016/j.neuroimage.2023.120219
7. Unnwongse K, Achakulvisut T, Wu JY, et al. Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. *Brain Communications*. 2023;5(2):fcad023.
   - https://doi.org/10.1093/braincomms/fcad023
8. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025;66(11):4451-4464.
   - https://doi.org/10.1111/epi.18552
9. Feng Z, Guan C, Sun Y. Block-Champagne: A novel Bayesian framework for imaging extended E/MEG source. *IEEE Transactions on Medical Imaging*. 2025.
   - https://doi.org/10.1109/TMI.2025.3642620
