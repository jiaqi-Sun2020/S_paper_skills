# QCT/QWCT Scientific Narrative Methodology

Read this reference before drafting or revising a QCT/QWCT abstract, introduction, contribution paragraph, results overview, or discussion. It is a reusable writing methodology, not a one-paper patch.

## Core Principle

Write the paper as a scoped physics-methodology claim:

```text
Under a specified quantum-walk model and data regime,
sparse position probabilities can be used as a diagnostic of coin-state observability.
```

Do not write it as a universal theorem unless identifiability, noise, masks, dimensions, and baselines have been proved or exhaustively tested.

## Claim Ladder

Use this hierarchy when choosing wording:

1. **Setting**: specify Grover coin, shift rule, initial walker position, step range, simulated noiseless probabilities, training/test distribution, and mask construction.
2. **Question**: ask whether a restricted position-probability vector retains enough information to reconstruct the coin state within that setting.
3. **Method contribution**: define the keep-k sparse-position diagnostic, including how positions are ranked or chosen.
4. **Evidence**: report the strongest completed regime first, then comparative regimes, then inconclusive high-dimensional extension.
5. **Boundary**: state what remains unproved: arbitrary states outside the training distribution, finite-shot noise, random masks, strong baselines, independent seeds, and identifiability.

## Abstract Method

A good abstract should follow this order:

1. Scoped opening, not a universal conclusion.
   - Prefer: "在特定 Grover 量子行走设置下，位置概率分布可能携带可用于硬币态重建的信息。"
   - Avoid: "离散时间量子行走把硬币态信息编码到位置概率分布中。"
2. Problem with boundary.
   - State whether the reconstruction is for simulated, noiseless, training-distribution test samples, finite-shot data, arbitrary pure states, or density matrices.
3. Contribution sentence.
   - Name the reusable contribution, e.g. "keep-k 稀疏位置可观测性诊断方案" in Chinese author-review manuscripts, or "sparse-position observability diagnostic" in final English manuscripts.
4. Method summary.
   - Explain that the work trains/evaluates an inverse estimator on simulated Grover-walk probability distributions; do not mention internal code names.
5. Evidence hierarchy.
   - Put interpretation before numbers. Use numbers sparingly and only for completed evidence.
6. Formal limitation.
   - Use publication language such as "高维推广仍不确定" instead of progress language such as "目前只有部分 eval" or "未完成证据".

## Introduction Method

Use five paragraph jobs:

1. **Context and gap**: quantum state tomography infers latent states from measurement statistics; quantum walks couple coin and position degrees of freedom; prior work motivates the setting but does not make sparse position observability trivial.
2. **Why the inverse problem is nontrivial**: influence is not invertibility. Position probabilities discard complex amplitudes and phases, the map can be non-injective, different coin states may induce similar distributions, and finite masks can remove discriminative positions.
3. **Why sparse positions matter**: motivate detector cost, restricted access, compressed measurement, and observability diagnosis before presenting technical mask definitions.
4. **Positive contribution statement**: say what the paper proposes and tests. Do not write internal reminders such as "the contribution should not be described as...".
5. **Paper organization**: use neutral section descriptions. Do not mention "PRA style" or "author-review" in the manuscript body.

## Contribution Types

Choose explicit contribution language:

- **Diagnostic scheme**: a keep-k sparse-position observability diagnostic. In Chinese manuscripts, write "诊断方案" or "诊断流程" rather than mixing in `protocol`.
- **Empirical finding**: high-fidelity reconstruction is observed in a specified 4D Grover plane-walker regime.
- **Comparative boundary**: 2D and 6D settings identify limits rather than supporting universal scalability.
- **Measurement insight**: position selection and walk step affect how coin information appears in probability observations.

Avoid vague phrases such as "diagnosis" alone unless the diagnostic procedure and output curve are defined.

## Result Reporting Method

- Do not place raw experiment numbers before the reader knows the method and contribution.
- Report completed evidence as completed evidence; report partial evidence as a scoped subset, not an internal process failure.
- Replace internal language:
  - "QCT_run_all" -> "simulated Grover-walk probability distributions" or a formally defined software artifact only after definition.
  - "partial eval aggregation" -> "the evaluated 6D step-3 subset".
  - "step 4 has no checkpoint" -> "step-4 6D evidence is not included in the present comparison".
  - "下一步实验" in body -> "limitations and future work".
  - "PRA 风格组织" -> remove from manuscript body.

## Terminology Rules

On first use, write Chinese and English once only when the English term is necessary. For Chinese author-review manuscripts, prefer the Chinese term afterward and avoid English workflow words.

- 硬币态 (coin state)
- 位置概率分布 (position probability distribution)
- 位置掩码 (position mask)
- keep-k 稀疏位置观测
- 逆估计器 (inverse estimator)
- 保真度 (fidelity)
- 可观测性诊断 (observability diagnostic)

Avoid mixing `claim`, `pipeline`, `eval`, `checkpoint`, `author-review`, or other workflow terms into formal manuscript prose.

## Forbidden Or Needs-Definition Phrases

Do not use these unless explicitly defined and supported:

- "结构化的层析测量前处理"
- "量子行走把硬币态信息编码到位置概率分布中" as an unrestricted statement
- "证明稀疏位置测量可以层析任意硬币态"
- "普适高维层析结论"
- "神经网络提高了重建性能" as the central contribution
- internal code or workflow names in abstract/introduction

## Abstract/Introduction Checklist

Before finalizing, check:

- The first abstract sentence has a setting qualifier.
- The abstract names one reusable contribution.
- The abstract separates method, evidence, and limitation.
- The introduction explains why influence does not imply invertibility.
- keep-k has a physical or diagnostic meaning, not only a machine-learning feature-selection meaning.
- Negative or inconclusive evidence is framed as boundary mapping.
- No internal writing-process terms appear in the manuscript body.