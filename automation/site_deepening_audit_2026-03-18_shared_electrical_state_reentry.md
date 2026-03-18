# Site Deepening Audit (2026-03-18, Shared Extracellular / Electrical State Re-entry)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`

## 今回の選定理由

- 2026-03-18 時点で公開サイトは、`cell type`、`transcription / chromatin`、`proteostasis`、`ECM / PNN`、`ionic milieu / chloride`、`timing-state` をかなり厳密に分離できておりました。
- しかし、`chemical connectome の外にある shared extracellular / electrical state` は、主要ページでは再び `omitted mechanisms` の脚注に近い位置へ後退しており、独立 class として前景化されていませんでした。
- さらに、`automation/site_deepening_audit_2026-03-17_shared_extracellular_electrical_state.md` には本体反映済みと記録されている一方で、現行の公開本文ではその記述が十分に残っておらず、監査記録と本文の整合が崩れておりました。

## 根拠付き批判

### 1. 現行 front door は `chemical synapse graph` と `electrical-state` の差を十分に止めていませんでした

- 問題:
  - `wbe_101.md` は hidden-state をよく整理していましたが、`shared extracellular / electrical state` が表に無く、connectome route の missing item でも `electrical synapses` が omitted mechanism の 1 つとしてしか読めませんでした。
  - そのため、読者が `chemical connectome + nominal inhibition` を `fast synchrony もかなり固定された` と誤読する余地が残っておりました。
- 根拠:
  - Galarreta & Hestrin (1999) は neocortical fast-spiking interneuron 間の electrical coupling を示しました。
  - Anastassiou et al. (2011) は endogenous extracellular field が cortical spike timing を causally entrain しうることを示しました。
  - Yang et al. (2024) は dynamic electrical synapses が persistent oscillation と epileptogenesis に関与することを示しました。
- 批判:
  - したがって、`chemical wiring が分かる` と `electrical coupling / electrotonic regime が分かる` は別問題でございます。
  - ここを front door で止めないと、`connectome-complete ≈ electrical-state-complete` という過大読みに戻ります。

### 2. 旧 verification gate は `inhibitory sign` までは止めていたが、`electrical coupling / field state` を submission gate に落としていませんでした

- 問題:
  - `verification.md` には `ionic milieu / chloride homeostasis` の独立 gate があり、これは妥当でした。
  - しかし、`gap junction`、`endogenous field`、`local inhibitory driving force` が同時に関わる fast synchrony / oscillatory coordination については、独立 state class と augmentation claim がありませんでした。
- 根拠:
  - Selfe et al. (2024) は ORCHID により inhibitory receptor driving force を in vivo で直接測定できることを示しました。
  - これは裏返すと、`E_GABAA / DF_GABAA` は専用の局所計測を要する変数であり、chemical connectome や macro proxy から自動では回収できないことを意味します。
- 批判:
  - したがって、verification 側も `chemical connectome は electrical-state complete ではない` と card / gate で明示する必要がありました。

### 3. human evidence も `direct readout` ではなく `perturbation-conditioned clue` に留めるべきでした

- 問題:
  - 共有電気状態について、human side にどこまで言えるかが主要ページで固定されていませんでした。
- 根拠:
  - Feld et al. (2026) は healthy participants において mefloquine 前投与が declarative-memory retention と spindle-to-slow-oscillation coupling を損ねることを示しました。
  - ただし同論文自身が off-target effects を完全には除外しておらず、これは local electrical coupling の direct readout ではありません。
- 批判:
  - よって、human evidence は `electrical state exists and matters` の perturbation clue にはなっても、`which cells were electrically coupled` や `local inhibitory driving force` の ground truth には上がりません。
  - この ceiling を本文で固定しないと、human sleep-memory result を electrical-state observability の証明へ誤昇格させます。

## 今回実行した変更

- `wbe_101.md`
  - page highlights / known points に `shared extracellular / electrical state` を追加
  - hidden-state overview paragraph に electrical-coupling / ephaptic / inhibitory-driving-force literature を追加
  - hidden-state table に `Shared extracellular / electrical state` row を追加
  - route comparison の connectome row を `chemical connectome != electrical-state complete` へ更新
  - references に Galarreta & Hestrin (1999), Anastassiou et al. (2011), Yang et al. (2024), Selfe et al. (2024) を追加
- `wiki/connectome-is-not-enough.md`
  - front matter に `shared extracellular / electrical state` を反映
  - `10 state classes` を `11 state classes` に更新
  - state-class table に `Shared extracellular / electrical state` を追加
  - 専用節を追加し、gap junction / ephaptic field / inhibitory driving force を独立に説明
  - human 側は `perturbation-conditioned clue` として読む ceiling を追加
  - augmentation / ablation table と site rules に `shared extracellular / electrical-state audit` を追加
  - references に Galarreta & Hestrin (1999), Anastassiou et al. (2011), Yang et al. (2024), Selfe et al. (2024), Feld et al. (2026) を追加
- `verification.md`
  - page highlights / known points に `shared extracellular / electrical state` を追加
  - `state variable integrity gate` を `at least eleven state classes` に更新
  - gate table に `Shared extracellular / electrical state` row を追加
  - addendum に `chemical connectome is not electrical-state complete` を追加
  - augmentation table に `+ shared extracellular / electrical-state audit` row を追加
  - references に同上 5 本を追加

## 外部依存で保留

- なし
  - 今回の作業は、公開本文の改稿と監査記録の整合回復で完結しております。

## 参考文献

1. Galarreta M, Hestrin S. A network of fast-spiking cells in the neocortex connected by electrical synapses. *Nature*. 1999;402:72-75.
   - https://doi.org/10.1038/99496
2. Anastassiou CA, Perin R, Markram H, Koch C. Ephaptic coupling of cortical neurons. *Nature Neuroscience*. 2011;14(2):217-223.
   - https://doi.org/10.1038/nn.2727
3. Yang Y-C, Wang G-H, Chou P, Hsueh S-W, Lai Y-C, Kuo C-C. Dynamic electrical synapses rewire brain networks for persistent oscillations and epileptogenesis. *PNAS*. 2024;121(8):e2313042121.
   - https://doi.org/10.1073/pnas.2313042121
4. Selfe JS, et al. All-optical reporting of inhibitory receptor driving force in the nervous system. *Nature Communications*. 2024;15(1):8913.
   - https://doi.org/10.1038/s41467-024-53074-y
5. Feld GB, Niethard N, Liu J, et al. Electrical synapses contribute to sleep-dependent declarative memory retention. *European Journal of Neuroscience*. 2026;63(2):e70401.
   - https://doi.org/10.1111/ejn.70401
