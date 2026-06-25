# S Paper Skills

`S_paper_skills` 是一组本地 Codex skills，用来支持研究想法打磨、论文实验设计、训练代码架构、研究报告生成、LaTeX 论文交付，以及 skill 本身的创建和维护。

这些 skills 的默认应用场景是机器学习与科研论文工作流，例如图学习、物理启发模型、时序建模、多模态方法、优化算法和系统类方法。CTQW 与动态图神经网络只是其中一个应用示例，不是本仓库的唯一目标。

每个正式 skill 至少包含一个 `SKILL.md`，并在 frontmatter 中声明 `name` 和 `description`。Codex 主要依靠这两个字段识别 skill，因此新增、移动或修改 skill 后都应运行校验。

## Skill Overview

### Research Skills

| Skill | Path | Purpose |
|---|---|---|
| `research-logic` | `research-logic-skill/` | 分析两个研究方法、模型、理论或机制如何形成机制级结合，而不是停留在模块拼接。 |
| `experiment-design` | `experiment-design-skill/` | 将模型想法转化为论文级实验设计，包括 research questions、datasets、baselines、ablations、metrics、mechanism checks 和 claim boundaries。 |
| `data-analysis` | `data-analsys-skill/` | 分析实验数据和论文结果，包含完整性检查、统计检验、effect size、confidence interval 和 claim 支撑边界。 |
| `research-html-report` | `research-html-report/` | 将研究逻辑、创新点、实验设计、风险边界和下一步计划整理成独立 HTML research brief 或 publication-style report。 |
| `training-code-architecture` | `training-code-architecture-skill/` | 生成或重构可复用的机器学习训练代码架构，强调 config-driven training、factories、adapters、checkpoint、logs 和 CSV results。 |
| `latex-paper-build-skill` | `latex-paper-build-skill/` | 将已有 `.tex` 论文或新论文项目整理成完整 LaTeX manuscript framework 和 paper delivery pipeline。 |

### Utility Skills

| Skill | Path | Purpose |
|---|---|---|
| `interactive-skill-builder` | `util_skills/interactive-skill-builder/` | 通过作者访谈、规格确认和预创建审核来创建或更新 Codex skill。 |
| `skill-audit-refactor` | `util_skills/skill-audit-refactor/` | 审核、精简、重构或拆分已有 skill，减少上下文占用，同时保留关键能力。 |
| `project-agent-generator-skill` | `util_skills/project-agent-generator-skill/` | 为陌生项目生成 `.agents/` 或 `.agent/` 上下文目录，包含 AGENTS、项目背景、架构、配置、运行手册和决策记录。 |

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

### `training-code-architecture`

用于设计或生成可复用的机器学习训练代码架构。它保留 architecture，而不绑定某个具体任务、模型或数据集。

核心约定：

- `main.py -> train(args)` 的薄入口；
- config-driven training；
- factories 负责模型、优化器和调度器构造；
- adapters 隔离任务相关的数据、forward、loss 和 metrics；
- 统一保存 checkpoint、logs、config copy 和 CSV results；
- 通过 adapters 兼容 static graph、dynamic graph、sequence modeling、classification 或 regression 等任务。

常用命令：

```powershell
python training-code-architecture-skill\scripts\create_project.py --help
```

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

### `skill-audit-refactor`

用于审核、精简、重构或拆分其他 Codex skills。它关注 context cost、trigger 质量、资源拆分和验证完整性。

适合问题：

- 某个 skill 是否太长、太宽泛或重复；
- `description` 是否能正确触发；
- 是否需要拆分成多个 skill；
- 哪些内容应保留在 `SKILL.md`，哪些应移动到 `references/`、`scripts/` 或 `assets/`；
- 精简后如何验证能力没有下降。

### `project-agent-generator-skill`

用于给陌生代码项目生成 agent-facing 上下文包，帮助后续 Codex/AI agent 不依赖聊天记录也能接手项目。默认输出 `.agents/`，包含 `AGENTS.md`、`PROJECT_CONTEXT.md`、`ARCHITECTURE.md`、`CONFIG_SPEC.md`、`RUNBOOK.md`、`DECISIONS.md` 和 `README.md`；如果用户明确要求，也可生成 `.agent/`。

适合问题：

- 给一个陌生项目生成 agent onboarding 文件；
- 把项目架构、运行命令、配置入口和决策记录沉淀到仓库；
- 为未来会话保留稳定项目上下文；
- 刷新已有 `.agents/` 文档并检查命令、路径和推断是否可信。

常用命令：

```powershell
python util_skills\project-agent-generator-skill\scripts\generate_project_agents.py path\to\project --out-dir .agents --force
```

## Recommended Workflows

### Research Paper Pipeline

对于一个新的研究想法或模型方法，推荐按下面顺序使用：

```text
research-logic
-> experiment-design
-> data-analysis
-> research-html-report
-> training-code-architecture
-> latex-paper-build-skill
```

含义：

1. 判断多个方法之间是否形成机制级结合，而不是简单模块拼接。
2. 设计能支撑论文 claim 的实验方案。
3. 分析实验数据、统计显著性、效应量、置信区间和 claim 支撑边界。
4. 生成 HTML research brief 或 paper-style report。
5. 将模型和实验落到可复用训练代码架构中。
6. 整理 LaTeX 论文框架、编译路径和提交前检查。

### Skill Creation And Maintenance

对于创建或维护 skill，推荐按下面顺序使用：

```text
interactive-skill-builder
-> skill-audit-refactor
-> quick_validate.py
```

含义：

1. 通过作者访谈形成 skill 规格，并要求明确确认。
2. 用审核视角检查 scope、trigger、资源结构和验证计划。
3. 运行官方 validator，确保新增或修改后的 skill 可被 Codex 正确识别。

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
|-- research-html-report/
|   |-- SKILL.md
|   `-- agents/openai.yaml
|-- training-code-architecture-skill/
|   |-- SKILL.md
|   |-- README.md
|   |-- scripts/create_project.py
|   `-- templates/
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
    |-- skill-audit-refactor/
    |   |-- SKILL.md
    |   `-- agents/openai.yaml
    `-- project-agent-generator-skill/
        |-- SKILL.md
        |-- agents/openai.yaml
        |-- scripts/generate_project_agents.py
        `-- references/
```

## Validation

修改或新增 skill 后，运行：

```powershell
python C:\Users\SSS\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\AI\skill\S_paper_skills\<skill-folder>
```

示例：

```powershell
python C:\Users\SSS\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\AI\skill\S_paper_skills\data-analsys-skill
python C:\Users\SSS\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\AI\skill\S_paper_skills\latex-paper-build-skill
python C:\Users\SSS\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\AI\skill\S_paper_skills\util_skills\interactive-skill-builder
python C:\Users\SSS\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\AI\skill\S_paper_skills\util_skills\skill-audit-refactor
python C:\Users\SSS\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\AI\skill\S_paper_skills\util_skills\project-agent-generator-skill
```

如果新增脚本，也应运行对应的语法或 smoke test，例如：

```powershell
python -m py_compile latex-paper-build-skill\scripts\create_paper_pipeline.py
```

## Naming Rules

- `SKILL.md` 的 `name` 使用小写字母、数字和 hyphen，例如 `research-logic`。
- 文件夹名可以带 `-skill` 后缀；新增 skill 时优先让文件夹名与 `name` 保持一致。
- `description` 应说明能力和触发场景，不要只写泛泛的用途。
- 通用维护类 skill 放在 `util_skills/` 下。

## Maintenance Notes

- 不要在 skill 中写入虚假论文引用、虚假实验结果或不可复现指标。
- 大段参考资料放到 `references/`，不要塞进 `SKILL.md`。
- 可复用脚本放到 `scripts/`，模板文件放到 `templates/` 或 `assets/`。
- 创建新 skill 时优先使用 `util_skills/interactive-skill-builder/`，先完成作者访谈、规格确认和预创建审核。
- 审核或精简已有 skill 时使用 `util_skills/skill-audit-refactor/`。
- 更新 README 时，同步检查实际目录、`SKILL.md` frontmatter、资源文件和可用命令是否一致。

## License

See [LICENSE](./LICENSE).
