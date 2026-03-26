# Site Deepening Audit (2026-03-26, Literature Hubs Neurovascular / BBB Sync)

## 対象

- 主対象: `mind_uploading_papers.md`
- 主対象: `research_harvest_50.md`
- 生成更新: `summary_booklet.md`
- 同期参照: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 同期参照: `wbe_101.md`
- 同期参照: `verification.md`

## 今回の選定理由

- 2026-03-26 時点で、core pages 側では `neurovascular-unit / BBB / pericyte state` が maintenance-side family としてすでにかなり明示されていました。
- 一方で literature hub である `mind_uploading_papers.md` と `research_harvest_50.md` では、その整理がまだ弱く、読者が `vascular confound / CVR audit を見た = neurovascular maintenance biology も押さえた` と誤読しうる余地が残っていました。
- これは技術・自然科学の観点で優先度が高いです。一次文献が押し上げているのは、pericyte / BBB biology が単なる vascular nuisance ではなく、capillary support、plasticity、memory、そして human BBB permeability proxy の ceiling を別々に規定するという点だからです。

## 根拠付き批判

### 1. literature hubs が core pages の reading rule に追いついていませんでした

- 問題:
  - site-wide ではすでに `neurovascular-unit / BBB / pericyte state` を maintenance-side family として扱っていました。
  - しかし literature hubs では、maintenance-state row や human observability row の中に十分に表出しておらず、front-door で読んだ読者が重要 split を見落としえました。
- 批判:
  - `index.md` や `verification.md` だけが厳密で、literature hub が旧い reading rule のままだと、混在アーカイブの入口で再び誤読を誘発します。hub page こそ route-family split を露出すべきでした。

### 2. pericyte / BBB biology は generic vascular nuisance や generic clearance に吸収してはいけません

- 根拠:
  - [Bell et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.043) は pericyte deficiency が cerebral blood flow、BBB integrity、neuronal phenotype に関わることを示しました。
  - [Kisler et al. (2020)](https://doi.org/10.3389/fncel.2020.00027) は cortical pericyte ablation が rapid neurovascular uncoupling を起こすことを示しました。
  - [Pandey et al. (2023)](https://doi.org/10.1016/j.neuron.2023.08.030) は pericyte-derived IGF2 signal が long-term memory formation に関わることを示しました。
  - [Swissa et al. (2024)](https://doi.org/10.7554/eLife.89611) は cortical plasticity と BBB modulation の連動を示しました。
  - [Mai-Morente et al. (2025)](https://doi.org/10.1038/s41467-025-61312-0) は pericyte Panx1 route が capillary diameter control と memory function に関与することを示しました。
- 批判:
  - したがって、pericyte / endothelial / BBB route は `clearance / immune support` や `hemodynamic confound` へ圧縮してよいものではありません。maintenance-side controller family として別立てが必要でした。

### 3. human BBB route は重要ですが、なお macro proxy ceiling を持ちます

- 根拠:
  - [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) は multi-echo ASL による BBB water permeability route を示しました。
  - [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は PET と kinetic modeling による molecular BBB permeability route を示しました。
- 批判:
  - これらは human observability を押し上げる重要な route ですが、なお `macro permeability / exchange proxy` です。cell-specific pericyte controller や local BBB maintenance logic を直接読む route ではありません。したがって human proxy table に独立 row と claim ceiling の明示が必要でした。

### 4. literature hubs では controller-side biology と human proxy ceiling を同時に見せる必要がありました

- 問題:
  - 旧記述では、controller-side neurovascular biology と human BBB permeability route が同じ段落や generic support language に埋もれやすい構造でした。
- 批判:
  - 自然科学的には、この二つは同じ inferential object ではありません。
  - `pericyte / BBB controller biology`
  - `human macro BBB proxy`
  を並置し、それぞれの evidential gain と claim ceiling を別々に書かないと、reader は `human route がある = controller state に近づいた` と読み替えやすくなります。

## 今回実行した変更

- `mind_uploading_papers.md`
  - 2026 technical addendum を `five explicit corrections` に更新し、neurovascular / BBB / pericyte route-family split を追加
  - priority route table に `neurovascular / BBB / pericyte route-card split` row を追加
  - `human in vivo observability / proxy ladder` に Padrela / Chung を追加し、`macro BBB permeability / exchange proxy` と calibrator role を明記
  - `maintenance-state / mechanistic boundary` に neurovascular-unit / BBB / pericyte support を追加
  - neurovascular / BBB evidence を independent maintenance-side route として読む note-box を追加
  - evidence-class table にも BBB proxy ceiling と neurovascular hidden-state family を反映

- `research_harvest_50.md`
  - front matter と priority route の maintenance-state description に `neurovascular-unit / BBB / pericyte support` を追加
  - `Read human measurement papers as their own evidence class` に Padrela / Chung を統合し、BBB proxy row を追加
  - `Read neurovascular / BBB evidence as a separate U3 route` の note-box を追加
  - U3 の current traction / unresolved / representative references / major previous studies を更新し、controller-side biology と human proxy ceiling の両方を入れました
  - paper-level anchors note でも neurovascular / BBB route-family split を front-door から見えるようにしました

- `summary_booklet.md`
  - 上記ページ変更を要約側へ再反映する前提で再生成対象にしました

## 外部依存で保留

- なし
  - 今回の修正は、このリポジトリ内の公開本文・要約再生成で完結しています。

## 参考文献

1. Bell RD, Winkler EA, Sagare AP, et al. Pericytes control key neurovascular functions and neuronal phenotype in the adult brain and during brain aging. *Neuron*. 2010;68(3):409-427.
   - https://doi.org/10.1016/j.neuron.2010.09.043
2. Kisler K, Nikolakopoulou AM, Sweeney MD, et al. Acute ablation of cortical pericytes leads to rapid neurovascular uncoupling. *Front Cell Neurosci*. 2020;14:27.
   - https://doi.org/10.3389/fncel.2020.00027
3. Pandey K, Bessières B, Sheng SL, et al. Neuronal activity drives IGF2 expression from pericytes to form long-term memory. *Neuron*. 2023;111(23):3819-3836.e8.
   - https://doi.org/10.1016/j.neuron.2023.08.030
4. Swissa E, Monsonego U, Yang LT, et al. Cortical plasticity is associated with blood-brain barrier modulation. *eLife*. 2024.
   - https://doi.org/10.7554/eLife.89611
5. Mai-Morente S, Razvan M, Lechuga-Sancho AM, et al. Pericyte pannexin1 controls cerebral capillary diameter and supports memory function. *Nat Commun*. 2025;16:5912.
   - https://doi.org/10.1038/s41467-025-61312-0
6. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiol Aging*. 2025;147:176-186.
   - https://doi.org/10.1016/j.neurobiolaging.2024.12.012
7. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nat Commun*. 2025;16:3076.
   - https://doi.org/10.1038/s41467-025-58356-7
