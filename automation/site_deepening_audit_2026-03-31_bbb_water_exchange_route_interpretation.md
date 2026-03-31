# Site Deepening Audit (2026-03-31, BBB water-exchange route interpretation)

## 対象

- 主対象:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 同期対象:
  - `index.md`
  - `wbe_101.md`
  - `verification.md`
  - `github-wiki-export/homeostatic-plasticity-and-maintenance-state.md`
- 調査範囲:
  - 技術
  - 自然科学

## web確認対象

- `https://doi.org/10.1016/j.neuroimage.2018.12.026`
- `https://doi.org/10.1002/nbm.5256`
- `https://doi.org/10.1016/j.neurobiolaging.2024.12.012`
- `https://doi.org/10.1016/j.nicl.2025.103926`
- `https://doi.org/10.1038/s41467-025-58356-7`

## 今回この箇所を選んだ理由

- site はすでに `neurovascular / BBB / pericyte state` を `vascular-state / CVR audit` から分離しておりました。
- しかし human BBB 側の公開文言には、なお `ASL-based Tex/Kw` を暗黙に `generic BBB leakiness meter` と読める余地が残っておりました。
- この弱点は technical であり、哲学や法学の問題ではございません。
  - `ASL water-exchange`
  - `tracer-specific PET permeability-surface-area`
  - `contrast leakage`
  は同じ quantity family ではなく、同じ carrier / boundary / model burden でもございません。
- さらに 2026 年の新しい human paper により、`Tex` は amyloid-specific な meter でもないことが明瞭になりました。

## 主要結論

- current human BBB evidence は一つの `permeability scalar` ではございません。
- この site では少なくとも以下を分けて書かなければなりません。
  - `ASL-derived water-exchange time / rate`
  - `blood-brain-interface water transport interpretation`
  - `tracer-specific PET PS`
  - `contrast-agent leakage`
- とくに `Tex` は
  - flow-free barrier scalar
  - generic leakiness scalar
  - amyloid-specific meter
  のいずれとしても無条件に読めません。

## 根拠付き批判

### 1. ASL 側 quantity は route-free permeability scalar ではございません

- 根拠:
  - [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) は multi-echo ASL による adult lifespan route であり、gray-matter age effect は `CBF` と `ATT` の補正後に消失しております。
  - [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256) は同一 cohort でも `DP-ASL` と `ME-ASL` が異なる BBB water-exchange 値と不一致な age dependence を返しうることを示しております。
- 批判:
  - この時点で、ASL-derived `Tex/Kw` を one interchangeable permeability meter として front door に置くのは不正確でございます。
  - 少なくとも acquisition family と fitting route を明示しなければ、quantity type が崩れます。

### 2. ASL 側は blood-brain-interface の水輸送感受性を含み、単なる leakiness ではございません

- 根拠:
  - [Ohene et al. (2019)](https://doi.org/10.1016/j.neuroimage.2018.12.026) は multi-TE ASL exchange time が AQP4 loss に感受的であることを示し、`blood-brain interface` の水輸送 route sensitivity を明示しております。
- 批判:
  - この literature を踏まえると、site が `ASL water exchange` を generic endothelial leakiness scalar のように読める余地を残すのは technical に弱いです。
  - human で AQP4 を直接読んだと言っているわけではございませんが、少なくとも `dominant transport interpretation` を黙らせてはいけません。

### 3. 2026 年 paper により Tex は amyloid-specific meter ではないことがさらに明瞭になりました

- 根拠:
  - [Padrela et al. (2026)](https://doi.org/10.1016/j.nicl.2025.103926) は older adults で `Tex` が `SCD / MCI` と moderate `WMH` burden で低下し、amyloid-group difference は age / sex adjustment 後に残らないことを示しております。
- 批判:
  - したがって `human BBB water-exchange route exists` を `AD-specific BBB meter exists` へ読み替えることはできません。
  - この site では `cognitive / cerebrovascular burden sensitive but not amyloid-specific under current adjustment` という ceiling を明記すべきでございます。

### 4. PET 側は tracer-specific kinetic quantity であり、ASL 側と同じ object ではございません

- 根拠:
  - [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は 3 radiotracers に対する dynamic PET kinetic modeling により BBB permeability-surface-area product を扱っております。
- 批判:
  - ここで得られる `PS` は tracer-specific transport mechanism と model assumption に依存しており、ASL-side `Tex/Kw` と one scalar に圧縮できません。
  - 従って public wording では `carrier / crossed boundary / model burden` を必ず書く必要がございます。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `How this site reads current human BBB evidence` に `Ohene et al. (2019)` と `Padrela et al. (2026)` を追加し、ASL water-exchange を
    - route-free leakiness scalar
    - amyloid-specific meter
    として読めないことを明文化しました。
  - `2026-03-31 addendum` を強化し、human BBB route card に `dominant transport interpretation` を要求する文言へ更新しました。
  - route-card table に `Interface sensitivity / dominant transport interpretation` 行を追加しました。
  - references に `Ohene 2019` と `Padrela 2026` を追加しました。

- `index.md`
  - front door の vascular note へ `Ohene 2019` と `Padrela 2026` を追加し、human BBB proxy は `quantity type, carrier, dominant transport interpretation` を開示しない限り overread できないようにしました。

- `wbe_101.md`
  - observability ladder の BBB row を `BBB / blood-brain-interface water-exchange and tracer-specific transport proxy` に更新しました。
  - BBB note-box に `Ohene 2019` と `Padrela 2026` を追加し、route-card field に `interface sensitivity / dominant transport interpretation` を追加しました。

- `verification.md`
  - vascular transfer audit addendum を更新し、`human BBB proxy exists` から `generic BBB-permeability meter exists` への飛躍をさらに止めました。

## 今回止めた誤読

- `ASL Tex/Kw` = generic BBB leakiness scalar
- `ASL Tex/Kw` = amyloid-specific BBB meter
- `human BBB proxy exists` = `neurovascular support state is matched`
- `PET PS` = `ASL water exchange`
- `clean vascular nuisance audit` = `pericyte / BBB controller state solved`

## 検証結果

- `git diff --check`
  - pass
- `ruby scripts/export_github_wiki.rb`
  - pass
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - pass
- `bundle exec jekyll build`
  - pass

## 外部依存タスク

- なし
  - 今回の作業は一次文献確認、repo 内改稿、生成物同期、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Ohene Y, Harrison IF, Nahavandi P, et al. Non-invasive MRI of brain clearance pathways using multiple echo time arterial spin labelling: an aquaporin-4 study. *NeuroImage*. 2019;188:515-523.
   - https://doi.org/10.1016/j.neuroimage.2018.12.026
2. Morgan CA, Thomas DL, Shao X, et al. Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. *NMR in Biomedicine*. 2024;37(12):e5256.
   - https://doi.org/10.1002/nbm.5256
3. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiology of Aging*. 2025;147:176-186.
   - https://doi.org/10.1016/j.neurobiolaging.2024.12.012
4. Padrela BE, Tecelão S, Kirsebom B-E, et al. Blood-brain barrier water exchange in relation to amyloid, cognition and cerebrovascular burden. *NeuroImage: Clinical*. 2026;49:103926.
   - https://doi.org/10.1016/j.nicl.2025.103926
5. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025;16:3076.
   - https://doi.org/10.1038/s41467-025-58356-7
