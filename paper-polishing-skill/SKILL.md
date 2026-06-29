---
name: paper-polishing-skill
description: Translate, polish, and structurally revise author-approved scientific manuscripts for Nature, PRL, and PRA style. Use when Codex needs to turn a Chinese author-review manuscript into final English after user approval, polish English manuscript prose, audit PRL/PRA/Nature section logic, protect claims, preserve LaTeX labels/citations/equations, or enforce journal-specific abstract, title, introduction, results, discussion, and conclusion moves without inventing evidence.
---

# Paper Polishing Skill

## Purpose

Use this skill after the scientific content of a manuscript has been drafted or reviewed. It owns post-review language transformation and polishing, not experiment invention. It can polish English drafts directly, but its default role inside `S_paper_skills` is:

```text
Chinese author-review manuscript
-> user scientific/content approval
-> journal-targeted English translation and polishing
```

This skill inherits the discipline of `nature-polishing`: fix the argument before the sentence, protect the author's scientific core, and never hide weak logic under fluent prose. It extends that stance to PRL and PRA in addition to Nature-family writing.

## Hard Gates

- Do not perform a full Chinese-to-English final manuscript translation until the user states that the Chinese scientific content is approved or asks explicitly to translate despite pending review.
- Do not invent data, citations, baselines, theory, mechanisms, novelty claims, or limitations.
- Do not upgrade a planned, partial, or missing result into a completed result.
- Preserve numeric values, units, equations, figure/table references, LaTeX labels, citation keys, and BibTeX workflow unless the user explicitly asks for a technical correction.
- When evidence is incomplete, keep the boundary visible in the polished output and revision notes.

## Workflow

1. Identify the target journal style and task mode.
   - `nature`: broad conceptual significance, non-specialist accessibility, strong but bounded significance.
   - `prl`: one central physics result, fast motivation, compact evidence chain, strict claim discipline.
   - `pra`: complete physics context, reproducible method detail, careful notation, mechanisms, limitations, and parameter regimes.
   - `generic`: clear scientific English without venue-specific compression.
   - Modes: Chinese-to-English finalization, English polishing, section logic audit, title/abstract polish, LaTeX-safe revision.
2. Build a terminology ledger before rewriting.
   - Record canonical method names, abbreviations, physical quantities, metrics, datasets, symbols, and notation.
   - Use one canonical form throughout; do not vary technical terms for style.
3. Diagnose the highest-level problem first.
   - Paper type and venue fit.
   - Section job.
   - Paragraph logic.
   - Claim, evidence, boundary.
   - Sentence-level polish.
4. Load only the needed references.
   - Always read `references/claim-safety.md`.
   - For Nature, PRL, PRA, or target-style work, read `references/journal-styles.md`.
   - For Chinese drafts or Chinese-influenced English, read `references/translation-workflow.md`.
   - For `.tex` files or LaTeX snippets, read `references/latex-preservation.md`.
5. Rewrite in controlled passes.
   - Extract propositions and evidence before drafting prose.
   - Reconstruct missing logical links without adding new science.
   - Apply venue-specific compression or expansion.
   - Polish sentence mechanics last.
   - Report structural changes and unresolved evidence gaps.

## Output Contract

For passage-level work, return:

1. Polished text.
2. `Terminology ledger:` when a ledger is new or changed.
3. `Revision notes:` with 3-5 short bullets on logic, style, and claim-boundary changes.
4. `Needs author check:` only for unresolved scientific or terminology decisions.

For whole-manuscript or LaTeX work, preserve the user's file structure unless they ask for a rewrite. If editing files, keep references in `.bib` files and figures in `figures/` according to the paper-build rules.