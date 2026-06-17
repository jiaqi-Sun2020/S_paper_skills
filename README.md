# S_paper_skill

这是我自己整理和编写的一组 Codex skills，主要用于沉淀论文复现、模型训练工程、实验代码架构等常用工作流。

当前仓库还比较轻量，已包含的 skill 以“可复用的训练代码架构”为主，后续可以继续把自己的研究流程、代码模板、实验规范整理成独立 skill 放进来。

## Skills

### training-code-architecture

位置：

```text
training-code-architecture-skill/
```

用途：

- 从已有训练项目中抽取稳定的代码架构，而不是绑定某一个具体任务。
- 生成 `main.py -> train(args)` 风格的训练入口。
- 使用 config 驱动实验。
- 用 factories 隔离模型、优化器、调度器等构造逻辑。
- 用 adapters 隔离具体任务的数据加载、模型调用、loss 和 metrics。
- 统一保存 checkpoint、日志、配置副本和结果 CSV。
- 支持从静态图任务迁移到动态图、序列模型、图像模型等不同任务。

适合在这些场景使用：

- 想把一个已有论文代码整理成更清晰的训练工程。
- 想为新模型快速生成一套可复用训练模板。
- 想让不同实验共用统一的输出目录、日志和指标文件。
- 想把任务细节从训练循环中拆出来，避免每换一个任务就重写 `train.py`。

## Repository Structure

```text
S_paper_skill/
|-- README.md
|-- LICENSE
`-- training-code-architecture-skill/
    |-- SKILL.md
    |-- README.md
    |-- scripts/
    |   `-- create_project.py
    `-- templates/
        |-- config.json
        |-- main.py
        |-- train.py
        |-- train_all.py
        `-- src/
            |-- factories.py
            |-- adapters/
            `-- utils/
```

## How to Use

把本仓库中的 skill 目录放到 Codex skills 目录中，或者在本地 Codex 环境中引用这个仓库。

使用 `training-code-architecture-skill` 生成一个训练项目模板：

```bash
cd training-code-architecture-skill
python scripts/create_project.py --output ./my_training_project --force
```

然后进入生成的项目运行：

```bash
cd my_training_project
python main.py --config config.json
```

生成的项目是一个 architecture-first 的起点。实际使用时，通常只需要替换：

- `config.json` 中的数据、模型和训练配置
- `src/adapters/` 下的任务适配器
- `src/factories.py` 中的模型构造逻辑

尽量保持 `main.py` 和通用训练循环稳定，让任务差异集中在 adapter 层。

## Design Notes

这个仓库里的 skills 更偏向个人研究工程实践，而不是通用软件包。目标是把自己反复使用的经验固化下来：

- 入口简单
- 配置清楚
- 训练循环可复用
- 任务逻辑可替换
- 实验结果可追踪
- 后续消融分析方便整理

后续新增 skill 时，建议每个 skill 独立放在一个目录中，并包含：

- `SKILL.md`：给 Codex 使用的正式 skill 说明
- `README.md`：给人看的使用说明
- `scripts/`：可选的脚本入口
- `templates/`：可选的代码模板或文件模板

## License

This project is licensed under the terms of the [LICENSE](./LICENSE).
