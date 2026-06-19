# Research Method Skills

这个目录存放当前仓库使用的本地 Codex skills，主要服务于通用研究方法整合、论文创新设计、实验验证、研究报告生成和训练代码架构整理。

CTQW 与动态图神经网络只是这些 skills 的一个应用示例，不是本目录的唯一目标。后续也可以用于图学习、物理启发模型、时序模型、多模态模型、优化算法、系统方法或其他机器学习论文想法。

每个正式 skill 至少应包含一个 `SKILL.md`，并在 frontmatter 中声明 `name` 和 `description`。Codex 主要通过这两个字段识别 skill，因此新增或修改 skill 后需要运行校验。

## Available Skills

### research-logic

Path: `research-logic-skill/`

用于分析两个研究方法、模型或机制如何结合。重点不是简单拼接模块，而是判断一个方法是否改变了另一个方法的内部状态、动态假设、转移规则或数学机制。

适合问题：

- 两个研究方法、模型、理论或机制如何结合；
- 某个组合是否只是 `A + B` 模块堆叠；
- 如何从浅层融合推进到机制级贡献；
- 如何写出克制、可信的论文 claim。

### experiment-design

Path: `experiment-design-skill/`

用于把模型想法转化为论文级实验设计。它从 central claim 出发，反推 research questions、datasets、baselines、ablations、metrics、mechanism checks、failure cases 和 claim boundaries。

适合问题：

- 一个想法能否支撑论文；
- 需要哪些实验才能证明机制有效；
- 如何设计消融和对照实验；
- 如何避免只报性能而缺少机制证据。

### research-html-report

Path: `research-html-report/`

用于把研究逻辑、创新点、实验设计和风险边界整合成独立 HTML 网页。当前支持两种主要输出风格：

- research brief：适合快速展示论文思路、机制图、实验表、风险表和下一步计划；
- publication mode：借鉴 HTML-first 与 PubCSS 思路，生成可打印、论文风格的 HTML，包含 figure/table/equation/reference 编号和 print CSS。

适合问题：

- 把任意论文想法、模型设计或实验计划整理成网页；
- 生成 shareable research brief；
- 生成可打印的论文计划页或预印本风格 HTML；
- 将 research-logic 与 experiment-design 的输出可视化。

### training-code-architecture

Path: `training-code-architecture-skill/`

用于设计或生成可复用的机器学习训练代码架构。重点是保留 architecture，而不是绑定某个具体任务或模型。

核心约定：

- `main.py -> train(args)` 的薄入口；
- config-driven training；
- factories 负责模型、优化器、调度器构造；
- adapters 隔离任务相关的数据、forward、loss 和 metrics；
- 统一保存 checkpoint、logs、config copy 和 CSV results；
- 通过 adapters 兼容不同任务类型，例如 static graph、dynamic graph、sequence modeling、classification 或 regression。

可用脚本：

```powershell
python .agents\skills\training-code-architecture-skill\scripts\create_project.py --help
```

### skill-audit-refactor

Path: `skill-audit-refactor/`

用于审核、精简、重构或拆分其他 Codex skills。重点是在不损失实际能力的前提下减少上下文占用，并判断内容应该保留在 `SKILL.md`，还是移动到 `references/`、`scripts/`、`assets/`，或者拆成独立 skill。

适合问题：

- 某个 skill 是否太长、太宽泛或重复；
- `description` 是否能正确触发；
- 是否需要拆分成多个 skill；
- 哪些内容应该压缩、移动或删除；
- 精简后如何验证能力没有下降。

## Suggested Skill Workflow

对于一个新的研究想法或模型方法，推荐按下面顺序使用：

```text
research-logic
-> experiment-design
-> research-html-report
-> training-code-architecture
```

含义：

1. 先判断多个方法之间是否形成机制级结合，而不是简单模块拼接。
2. 再设计能支撑论文 claim 的实验方案。
3. 然后生成 HTML research brief 或 paper-style report。
4. 最后把模型和实验落到可复用训练代码架构中。

## Recommended Three-Step Research Flow

当目标是判断一个方法组合能否形成论文贡献，并输出最终研究报告时，优先使用下面三步：

1. `research-logic-skill`：找到合适的结合点。
   - 分析两个方法各自的原生功能、状态变量、转移规则和核心假设。
   - 先构造最直接的浅层融合，再判断它是否只是模块拼接。
   - 回到方法的核心机制，寻找能改变状态转移、动态假设或内部逻辑的机制级结合点。

2. `experiment-design-skill`：设计相应的实验规划，保证论文可行性。
   - 以 central claim 为起点，反推 research questions、datasets、baselines、ablations、metrics 和 mechanism checks。
   - 以 PRA 为标准，即 paper-ready and reviewer-aware：实验必须能支撑论文主张，也要能回应审稿人对机制、baseline、消融、复杂度和失败场景的质疑。
   - 明确 claim boundaries：哪些结果能支撑强主张，哪些结果只能支撑弱主张。

3. `research-html-report`：根据前两步生成最终报告。
   - 汇总研究逻辑、创新点、模型机制、实验规划、证据矩阵、风险边界和下一步计划。
   - 输出 standalone HTML，可选择 research brief 或 publication mode。
   - 不伪造引用、实验结果或指标；缺失证据必须以 `TODO` 明确标出。

示例应用：

- CTQW + 动态图神经网络；
- 神经 ODE + 时序预测；
- 图神经网络 + 物理约束；
- 多模态表示学习 + 因果机制；
- 新优化器、新 loss 或新训练范式的论文设计。

## Directory Structure

```text
.agents/skills/
|-- README.md
|-- LICENSE
|-- research-logic-skill/
|   `-- SKILL.md
|-- experiment-design-skill/
|   |-- SKILL.md
|   `-- agents/openai.yaml
|-- research-html-report/
|   |-- SKILL.md
|   `-- agents/openai.yaml
|-- skill-audit-refactor/
|   |-- SKILL.md
|   `-- agents/openai.yaml
`-- training-code-architecture-skill/
    |-- SKILL.md
    |-- README.md
    |-- scripts/create_project.py
    `-- templates/
```

## Validation

修改或新增 skill 后，运行：

```powershell
$env:PYTHONUTF8='1'
python C:\Users\SSS\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\<skill-folder>
```

例如：

```powershell
python C:\Users\SSS\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\research-html-report
```

## Naming Notes

- `SKILL.md` 的 `name` 应使用小写字母和 hyphen，例如 `research-logic`。
- 文件夹名可以带 `-skill` 后缀，但为了检索更稳定，推荐后续新增 skill 时让文件夹名与 `name` 尽量一致。
- `description` 应写清楚触发场景，不要只写一句泛泛的用途。

## Maintenance Notes

- 不要在 skill 中写入虚假论文引用、虚假实验结果或不可复现指标。
- 大段参考资料应放到 `references/`，不要塞进 `SKILL.md`。
- 可复用脚本放到 `scripts/`，模板文件放到 `templates/` 或 `assets/`。
- 更新 README 时，同步检查实际目录、`SKILL.md` frontmatter 和可用命令是否一致。

## License

See [LICENSE](./LICENSE).
