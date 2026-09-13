# S Paper Skills

`S_paper_skills` 是一组本地 Codex skills，用来支持研究想法打磨、论文实验设计、研究报告生成、LaTeX 论文交付、PRL 专项审稿准备，以及项目内 skill 的创建。

这些 skills 的默认应用场景是机器学习与科研论文工作流，例如图学习、物理启发模型、时序建模、多模态方法、优化算法和系统类方法。CTQW 与动态图神经网络只是其中一个应用示例，不是本仓库的唯一目标。

每个正式 skill 至少包含一个 `SKILL.md`，并在 frontmatter 中声明 `name` 和 `description`。Codex 主要依靠这两个字段识别 skill，因此新增、移动或修改 skill 后都应运行校验。

## Paper Pipeline Rule

- 默认给作者审核的论文稿使用中文，但行文逻辑按 PRL/PRA 标准组织：先给物理问题和核心机制，再给证据链、边界条件和可检验 claim。
- QCT/QWCT 论文必须先应用 `latex-paper-build-skill/references/qct-writing-methodology.md`：摘要首句限定物理设置，引言解释“影响不等于可逆”，贡献表述为 keep-k 稀疏位置可观测性诊断，结果按证据强弱和边界条件组织。
- 用户审核中文科学内容后，才使用 `paper-polishing-skill/` 做 Nature、PRL 或 PRA 风格的英文翻译、压缩和润色；除非用户明确要求跳过审核门。
- 面向 PRL 投稿时，再使用 `prl-manuscript-polisher` 执行当前 APS 规则核验、PRL fit、word-equivalent、claim–evidence、REVTeX 和可追踪 LaTeX 修改审计；投稿前必须重新核对 APS 官方页面。
- 中文论文、LaTeX、skill 文档和 `.agent/` 文档默认按 UTF-8 读写；在 Windows 上运行 Python 验证或脚本时先设置 `PYTHONUTF8=1`，避免中文被 GBK 误解码。
- 整篇 `.tex` 英文化使用 `paper-polishing-skill/references/latex-full-paper-translation.md`：按段落论证单元翻译，保留 LaTeX 结构，并在定稿前按表格/图/正文交叉核对 mask、数值、排名等重复结果 claim。
- 所有文献统一由 `.bib` 文件管理；所有论文图片统一放入单一 `figures/` 文件夹。
- 论文作者、单位、通讯地址、邮箱、关键词、致谢等基础信息统一由根目录 `paper_config.json` 管理。
## Skill Overview

### Research Skills

| Skill | Path | Purpose |
|---|---|---|
| `research-logic` | `research-logic-skill/` | 分析两个研究方法、模型、理论或机制如何形成机制级结合，而不是停留在模块拼接。 |
| `experiment-design` | `experiment-design-skill/` | 将模型想法转化为论文级实验设计，包括 research questions、datasets、baselines、ablations、metrics、mechanism checks 和 claim boundaries。 |
| `data-analysis` | `data-analsys-skill/` | 分析实验数据和论文结果，包含完整性检查、统计检验、effect size、confidence interval 和 claim 支撑边界。 |
| `research-html-report` | `util_skills/research-html-report/` | 将研究逻辑、创新点、实验设计、风险边界和下一步计划整理成独立 HTML research brief 或 publication-style report。 |
| `latex-paper-build-skill` | `latex-paper-build-skill/` | 将已有 `.tex` 论文或新论文项目整理成完整 LaTeX manuscript framework 和 paper delivery pipeline。 |

### Polishing Skills

| Skill | Path | Purpose |
|---|---|---|
| `paper-polishing-skill` | `paper-polishing-skill/` | Post-approval manuscript and full-LaTeX-paper translation/polishing for Nature, PRL, and PRA. It preserves claims, labels, citations, equations, UTF-8 Chinese/LaTeX handling, and bibliography/figure layout; it rewrites Chinese prose as paragraph-level academic argumentation and requires repeated result-list audits against canonical tables. |

### Utility Skills

| Skill | Path | Purpose |
|---|---|---|
| `interactive-skill-builder` | `util_skills/interactive-skill-builder/` | 通过作者访谈、规格确认和预创建审核来创建或更新 Codex skill。 |
| `prl-manuscript-polisher` | `util_skills/prl-manuscript-polisher/` | 对技术上完整的物理论文执行 PRL fit、长度、证据、结构、语言、REVTeX 和投稿就绪度审计，并可生成可追踪 LaTeX 修改。 |

## Skill Details

### `research-logic`

用于判断一个方法组合是否具有论文贡献。重点不是“把 A 放进 B”，而是识别一个方法是否改变了另一个方法的内部状态、动态假设、转移规则或数学机制。

适合问题：

- 两个研究方法、模型、理论或机制如何结合；
- 某个组合是否只是 `A + B` 模块堆叠；
- 如何从浅层融合推进到机制级贡献；
- 如何写出克制、可信的论文 claim。

### `experiment-design`

用于把模型想法转化为 reviewer-aware 的实验方案。它从 central claim 出发，反推 research questions、datasets、baselines、ablations、metrics、mechanism checks、failure cases 和 claim boundaries。

适合问题：

- 一个想法能否支撑论文；
- 需要哪些实验才能证明机制有效；
- 如何设计消融和对照实验；
- 如何避免只报性能而缺少机制证据。

### `data-analysis`

用于把 CSV、JSON、NPZ、pickle、训练日志或实验结果表转化为可复核的数据分析结论。它强调数据来源、缺失值、分组/seed/fold 结构、统计检验选择、p-value、effect size、confidence interval，以及结果是否足以支撑论文 claim。

适合问题：

- 分析实验结果表、训练日志或 grouped CSV；
- 比较多个方法、step、keep-k、seed 或 ablation 的表现；
- 选择合适的统计检验并解释显著性、效应量和置信区间；
- 审核 ground truth、指标定义、结果文件和 claim 是否一致；
- 生成数据分析报告或论文结果段落的证据边界。

### `research-html-report`

用于把研究逻辑、创新点、实验设计和风险边界整合成独立 HTML 网页。支持两类输出：

- `research brief`：适合快速展示论文思路、机制图、实验表、风险表和下一步计划；
- `publication mode`：生成可打印的论文风格 HTML，包含 figure/table/equation/reference 编号和 print CSS。

适合问题：

- 把论文想法、模型设计或实验计划整理成网页；
- 生成 shareable research brief；
- 生成可打印的论文计划页或预印本风格 HTML；
- 将 `research-logic` 与 `experiment-design` 的输出可视化。

### `latex-paper-build-skill`

用于把研究想法或已有 `.tex` 论文整理成完整论文交付 pipeline。它负责 LaTeX 架构、单体论文拆分、REVTeX/ctex/fontspec/BibTeX 约定、figure/bib 路径检查、XeLaTeX/latexmk 编译，以及提交前机械检查。

适合问题：

- 将已有单体 LaTeX 论文拆成可维护框架；
- 为论文创建 `main.tex`、`preamble.tex`、`frontmatter.tex`、`sections/`、`figures/` 和 `references/`；
- 生成从研究逻辑到提交检查的完整 paper pipeline；
- 检查 bib 漂移、图片路径、编译命令和提交前问题。

常用命令：

```powershell
python latex-paper-build-skill\scripts\create_paper_pipeline.py --project path\to\paper_pipeline --title "Paper Title"
python latex-paper-build-skill\scripts\scaffold_latex_paper.py --source path\to\paper.tex --out path\to\framework --copy-figures
```

### `interactive-skill-builder`

用于创建或更新 Codex skill。它不会直接写文件，而是先询问作者的具体需求、触发场景、输出形式、资源需求、目标路径、风险动作和验证方式，再形成规格说明，经过确认和预创建审核后才创建或修改 skill。

适合问题：

- 想把一个工作流沉淀成新的 Codex skill；
- 需要先问清楚作者需求，再决定 skill 名称、scope 和资源结构；
- 创建前需要确认 destination、trigger、references/scripts/assets 和验证计划；
- 更新 README 或 skill bundle 索引时，需要保持目录、frontmatter 和说明一致。

### `prl-manuscript-polisher`

用于把技术上完整的物理论文工程化为证据克制、面向广泛物理读者且符合 PRL 约束的 Letter。它先检查科学定义、中心 claim 与证据，再处理内容取舍、长度预算、语言和 LaTeX，不会为了“更有冲击力”而扩大结论。

适合问题：

- 判断论文是否满足 PRL 的重要性、创新性、广泛兴趣和篇幅要求；
- 把正文元素标记为 KEEP-CORE、COMPRESS-CORE、MOVE-END、MOVE-SM 或 DELETE；
- 生成 `PRL_AUDIT.md`、`PRL_CONTENT_MAP.md`、执行清单、修改稿和 changelog；
- 在保留公式、标签、引用和环境的前提下生成 `latexdiff`、`\rev{...}` 或逐项变更说明；
- 使用 `scripts/audit_tex.py` 进行章节字数、浮动体、公式、重复标签和风格风险预检。

## Recommended Workflows

### Research Paper Pipeline

对于一个新的研究想法或模型方法，推荐按下面顺序使用：

```text
research-logic
-> experiment-design
-> data-analysis
-> research-html-report
-> latex-paper-build-skill
-> paper-polishing-skill (after user approval)
-> prl-manuscript-polisher (for PRL submission)
```

含义：

1. 判断多个方法之间是否形成机制级结合，而不是简单模块拼接。
2. 设计能支撑论文 claim 的实验方案。
3. 分析实验数据、统计显著性、效应量、置信区间和 claim 支撑边界。
4. 生成 HTML research brief 或 paper-style report。
5. 整理 LaTeX 论文框架、编译路径和提交前检查。
6. 用户审核中文稿后，再用 `paper-polishing-skill` 按段落论证链翻译并润色为目标期刊英文终稿；整篇 `.tex` 翻译需读取 UTF-8 源文档，遵循 `references/latex-full-paper-translation.md`，并核对 mask、数值、排名等重复 claim。
7. 若目标期刊是 PRL，最后用 `prl-manuscript-polisher` 重新核验当前 APS 规则、中心物理结论、word-equivalent、End Matter/SM 边界、REVTeX 与可访问性。

### Skill Creation And Maintenance

对于创建或维护 skill，推荐按下面顺序使用：

```text
interactive-skill-builder
-> quick_validate.py
```

含义：

1. 通过作者访谈形成 skill 规格，并要求明确确认。
2. 运行官方 validator，确保新增或修改后的 skill 可被 Codex 正确识别。

## Directory Structure

```text
S_paper_skills/
|-- README.md
|-- LICENSE
|-- research-logic-skill/
|   `-- SKILL.md
|-- experiment-design-skill/
|   |-- SKILL.md
|   `-- agents/openai.yaml
|-- data-analsys-skill/
|   |-- SKILL.md
|   |-- agents/openai.yaml
|   `-- references/
|-- paper-polishing-skill/
|   |-- SKILL.md
|   |-- agents/openai.yaml
|   `-- references/
|-- latex-paper-build-skill/
|   |-- SKILL.md
|   |-- agents/openai.yaml
|   |-- scripts/
|   |-- references/
|   `-- assets/
`-- util_skills/
    |-- interactive-skill-builder/
    |   |-- SKILL.md
    |   |-- agents/openai.yaml
    |   `-- references/
    |-- prl-manuscript-polisher/
    |   |-- SKILL.md
    |   |-- README.md
    |   |-- references/prl-rules.md
    |   |-- scripts/audit_tex.py
    |   `-- templates/execution-checklist.md
    `-- research-html-report/
    |   |-- SKILL.md
    |   `-- agents/openai.yaml
```

## Validation

修改或新增 skill 后，运行：

```powershell
$validator = Join-Path ([Environment]::GetFolderPath('UserProfile')) '.codex\skills\.system\skill-creator\scripts\quick_validate.py'
python $validator ".\<skill-folder>"
```

示例：

```powershell
$validator = Join-Path ([Environment]::GetFolderPath('UserProfile')) '.codex\skills\.system\skill-creator\scripts\quick_validate.py'
python $validator ".\data-analsys-skill"
python $validator ".\latex-paper-build-skill"
python $validator ".\paper-polishing-skill"
python $validator ".\util_skills\research-html-report"
python $validator ".\util_skills\interactive-skill-builder"
python $validator ".\util_skills\prl-manuscript-polisher"
```

如果新增脚本，也应运行对应的语法或 smoke test，例如：

```powershell
python -m py_compile latex-paper-build-skill\scripts\create_paper_pipeline.py
```

## Naming Rules

- `SKILL.md` 的 `name` 使用小写字母、数字和 hyphen，例如 `research-logic`。
- 文件夹名可以带 `-skill` 后缀；新增 skill 时优先让文件夹名与 `name` 保持一致。
- `description` 应说明能力和触发场景，不要只写泛泛的用途。
- 项目内支持类 skill 可以放在 `util_skills/` 下。

## Maintenance Notes

- 不要在 skill 中写入虚假论文引用、虚假实验结果或不可复现指标。
- 大段参考资料放到 `references/`，不要塞进 `SKILL.md`。
- 可复用脚本放到 `scripts/`，模板文件放到 `templates/` 或 `assets/`。
- 创建新 skill 时优先使用 `util_skills/interactive-skill-builder/`，先完成作者访谈、规格确认和预创建审核。
- PRL 数值限制和投稿要求属于可变外部规则；每次投稿审计都要重新检查 `prl-manuscript-polisher` 中列出的 APS 官方来源。
- 更新 README 时，同步检查实际目录、`SKILL.md` frontmatter、资源文件和可用命令是否一致。

## License

See [LICENSE](./LICENSE).
