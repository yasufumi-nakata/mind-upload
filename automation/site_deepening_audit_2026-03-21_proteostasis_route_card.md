# Site Deepening Audit (2026-03-21, Local Proteostasis / Synaptic-Tagging Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`

## 今回の選定理由

- 公開サイトはすでに `local proteostasis / synaptic-tagging state` を重要 hidden-state として繰り返し挙げています。
- しかし、最近 route-card 化された `phospho-signaling`、`sleep replay`、`myelin`、`bioenergetic`、`astrocyte`、`clearance / immune` と比べると、proteostasis だけはまだ `証拠クラスの分解` が甘いままでした。
- このままでは、少なくとも次の異なる inferential object が同じ `proteostasis evidence` として読めてしまいます。
  - synaptic tag / capture eligibility
  - dendritic branch-level integration of protein-synthesis-dependent LTP
  - synthesis vs proteasome-dependent degradation balance
  - autophagy-linked local plasticity routes
  - turnover-resistant persistence or active state transfer
  - proteasome-capacity intervention with behavioral consequences
- 技術・自然科学の観点では、これらは direct observable、時間軸、空間スケール、因果強度、human observability ceiling が違います。したがって、同じ claim ceiling に置くのは不適切です。

## 主要な批判点

### 1. `current weight` と `late-stabilization route` の分離は書かれていたが、まだ不十分でした

- 問題:
  - 既存サイトは `weight snapshot != late stabilization` という方向性自体は正しかったです。
  - ただし、それだけでは `何が late-stabilization route の中身なのか` が粗すぎました。
- 根拠:
  - Frey & Morris (1997) は synaptic tagging 仮説を提案しました。
  - Shires et al. (2012) は生体ラットで synaptic tagging and capture を示しました。
  - Govindarajan et al. (2011) は、protein-synthesis-dependent LTP の preferred integrative unit が dendritic branch であることを示しました。
- 批判:
  - したがって、`tag is set somewhere`、`branch integrates PRPs`、`late-LTP persists` は同じ意味ではありません。
  - 旧版のままだと、tag-setting evidence と branch-level integration evidence が同じ重みで読めてしまいます。

### 2. `proteostasis` が synthesis/degradation balance と autophagy subtype を十分に分けていませんでした

- 問題:
  - 既存文言は `translation/degradation/autophagy remain balanced` と書いていましたが、proteostasis 内部の route family をまだ一段深く固定していませんでした。
- 根拠:
  - Fonseca et al. (2006) は late-LTP maintenance に protein synthesis と proteasome-dependent degradation のバランスが必要であることを示しました。
  - Pandey et al. (2021) は local autophagy-coupled translation が long-term memory formation に関与することを示しました。
  - Chang et al. (2024) は、activity-induced synaptic remodeling において degradative autophagy だけでなく secretory autophagy が別の役割を持つことを示しました。
- 批判:
  - したがって、`autophagy is involved` は単一の意味ではありません。
  - 少なくとも `degradation balance` と `secretory-autophagy-linked remodeling` は別の claim family として扱う必要があります。

### 3. `molecular turnover 下でも記憶が維持される` という論点が、route card なしでは過大解釈されやすいままでした

- 問題:
  - 現行サイトは Lee et al. (2022) と Thomas et al. (2025) を引用していましたが、これらを `proteostasis solved memory persistence` のように読ませない stop rule が入口にありませんでした。
- 根拠:
  - Lee et al. (2022) は active state transfer によって synaptic memory が molecular turnover をまたいで維持されうることを示しました。
  - Thomas et al. (2025) は、stable actin pool と spine geometry が synaptic tag の timescale で持続しうることを示しました。
- 批判:
  - したがって、`turnover-resistant persistence` は `current local controller is directly measured` と同義ではありません。
  - これは `candidate substrate / persistence mechanism` の系統であって、human whole-brain observability を引き上げる証拠ではありません。

### 4. `proteostasis intervention` と `proteostasis readout` がまだ分け切れていませんでした

- 問題:
  - 旧版では proteostasis の causal relevance は示されていましたが、`intervention` と `measurement` の違いが route-card レベルでは固定されていませんでした。
- 根拠:
  - Parker et al. (2025) は aged mouse brain の proteasome activity decline を示し、PSMB5 overexpression や proteasome activator により spatial learning / memory decline を緩和できることを示しました。
- 批判:
  - したがって、proteasome-capacity intervention は強い causal evidence ですが、これは `tagged branch was measured`、`PRP capture was observed`、`human local late-stabilization controller was identified` を意味しません。
  - 旧版のままだと、この差が submission-side で固定されませんでした。

### 5. human observability ceiling が他の maintenance-state family より明示的ではありませんでした

- 問題:
  - 既存サイトは `human routes do not directly tell us which spine or branch carried the tag` と書いていましたが、front door と verification rules にまで十分に波及していませんでした。
- 根拠:
  - 現在このサイトが扱う human-side routes は、SV2A PET、MRSI、31P-MRS、sodium MRI、dynamic DMI、myelin mapping、TMS-EEG、CSF proxies などです。
  - これらは branch-local PRP capture、local ribosome/proteasome/autophagy state、tag persistence、same-subject whole-brain late-stabilization controller を直接は分解しません。
- 批判:
  - したがって、human proxy-rich evidence が増えても、proteostasis route を silent に `nearly observed` 扱いしてはいけません。
  - ここは WBE の誤読が起きやすい重要点なので、verification でも route-card 化すべきでした。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `page_highlights` に `proteostasis evidence is not one class` を追加
  - `known_points` に proteostasis evidence family の分解を追加
  - `unknown_points` に proteostasis route-card mandatory fields の未確定点を追加
  - `#proteostasis-route-card` を新設し、claim family / integrative unit / direct observable / turnover window / perturbation route / human observability / abstention boundary を明文化
  - Chang et al. (2024) と Parker et al. (2025) を追加し、proteostasis を `tagging` だけでなく `autophagy subtype` と `proteasome-capacity intervention` まで分解
- `verification.md`
  - `page_highlights` に proteostasis route-card requirement を追加
  - maintenance-state budget の proteostasis 行を route-card 粒度へ改稿
  - `local proteostasis evidence now needs a route card` note を追加し、front-door な stop rule を強化
- `wbe_101.md`
  - page highlight に `proteostasis evidence is not one class` を追加
  - entry-point note box として `Local proteostasis evidence now gets its own route card` を追加
  - WBE 入門段階でも `tag/capture`, `branch-level integration`, `autophagy-linked plasticity`, `turnover-resistant persistence`, `proteasome-capacity intervention` を分離

## 外部依存タスク

- human-compatible external calibration for local proteostasis
  - 担当者: 外部の計測法・ベンチマーク設計者
  - 前提条件: same-subject bridgeable route が、tagged branch / PRP capture / local proteasome or autophagy state のどれかに対する外部較正を提供すること
  - 完了条件: このサイトが `human proxy` ではなく `externally calibrated local proteostasis route` と明記できる公開ベンチマークが存在すること

## 参考文献

1. Frey U, Morris RGM. Synaptic tagging and long-term potentiation. *Nature*. 1997;385:533-536.
   - https://doi.org/10.1038/385533a0
2. Shires KL, Da Silva BM, Hawthorne JP, et al. Synaptic tagging and capture in the living rat. *Nature Communications*. 2012;3:1246.
   - https://doi.org/10.1038/ncomms2250
3. Govindarajan A, Israely I, Huang SY, Tonegawa S. The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. *Neuron*. 2011;69(1):132-146.
   - https://doi.org/10.1016/j.neuron.2010.12.008
4. Fonseca R, Vabulas RM, Hartl FU, Bonhoeffer T, Nagerl UV. A balance of protein synthesis and proteasome-dependent degradation determines the maintenance of LTP. *Neuron*. 2006;52(2):239-245.
   - https://doi.org/10.1016/j.neuron.2006.08.015
5. Pandey K, Yu X-W, Steinmetz A, Alberini CM. Autophagy coupled to translation is required for long-term memory. *Autophagy*. 2021;17(7):1614-1635.
   - https://doi.org/10.1080/15548627.2020.1775393
6. Lee J, Chen X, Nicoll RA. Synaptic memory survives molecular turnover. *Proceedings of the National Academy of Sciences USA*. 2022;119(42):e2211572119.
   - https://doi.org/10.1073/pnas.2211572119
7. Chang YC, Gao Y, Lee JY, et al. Identification of secretory autophagy as a mechanism modulating activity-induced synaptic remodeling. *Proceedings of the National Academy of Sciences USA*. 2024;121(16):e2315958121.
   - https://doi.org/10.1073/pnas.2315958121
8. Parker D, Davidson K, Osmulski PA, et al. Proteasome augmentation mitigates age-related cognitive decline in mice. *Aging Cell*. 2025;24(3):e14492.
   - https://doi.org/10.1111/acel.14492
9. Thomas M, Bogaciu CA, Rizzoli SO, Fauth M. Long-term potentiation-induced changes in actin dynamics and spine geometry persist on the timescale of the synaptic tag. *Communications Biology*. 2025;8:1065.
   - https://doi.org/10.1038/s42003-025-08459-0
