---
name: research-html-report
description: Use when Codex needs to synthesize research logic, innovation points, paper outlines, experiment design, model claims, ablations, datasets, and mechanism analysis into a polished standalone HTML webpage or report. Use after research-logic or experiment-design outputs, or when the user asks to present research ideas as an HTML page, visual research brief, paper planning dashboard, shareable project summary, printable academic report, or paper-style HTML with figures, tables, equations, citations, and publication-like CSS.
---

# Research HTML Report

## Purpose

Use this skill to convert research reasoning into a clear, polished, standalone HTML webpage. The output should help the user inspect the whole paper idea at once: motivation, core claim, innovation points, method logic, experiment design, risks, and next steps.

This skill is an output-design layer. It can consume results produced by research-logic and experiment-design, then render them into an HTML artifact.

## Acknowledgement

This skill is inspired in part by [nexu-io/html-anything](https://github.com/nexu-io/html-anything), especially its HTML-first approach: treat HTML as the primary expressive medium rather than a mechanical export target from Markdown.

Do not copy project-specific branding, templates, or source text from that project into generated user reports unless the user explicitly asks for that style. Use the inspiration as a design principle: standalone HTML, deliberate layout, and content shaped for visual reading.

This skill is also inspired in part by PubCSS-style academic HTML publishing patterns: use semantic HTML and CSS counters to make web reports feel closer to printable research artifacts. Do not copy PubCSS source stylesheets wholesale; borrow the ideas of publication-grade structure, figure/table/equation numbering, print CSS, and citation-aware markup.

## Core Principle

Do not merely dump Markdown into HTML. Transform the research idea into a structured visual report.

Use this flow:

```text
research idea -> claim -> innovation points -> method logic -> experiment evidence -> risk boundaries -> HTML report
```

The HTML page should make the argument easier to evaluate, not just prettier.

## HTML-First Rules

Borrow these HTML-first principles:

- Treat the webpage as the final artifact, not as a wrapper around Markdown.
- Use layout to clarify thinking: grids for comparison, tables for evidence, cards for repeated claims, and code blocks for equations.
- Generate a complete `.html` file that opens directly in a browser.
- Prefer embedded CSS and inline SVG/CSS diagrams over external assets when a diagram is simple.
- Do not invent fake numbers, fake citations, fake datasets, or placeholder image URLs.
- If evidence is missing, mark it as a concrete TODO rather than hiding it behind polished design.
- Keep the page self-contained unless the user explicitly requests external libraries or assets.

## Research Brief Pattern

For research ideas that need to feel more polished than a plain document, use a visual research brief pattern.

Required elements:

- **Dual-zone hero**: left side states the research hook and central claim; right side shows 2-4 status cards such as contribution level, current evidence, best claim target, and next blocker.
- **Section kickers**: each major section should have a short label such as `Problem Gap`, `Claim`, `Innovation Map`, `Method Logic`, `Experiment Design`, `Evidence Matrix`, `Risk Ledger`, or `Minimum Viable Plan`.
- **Inline logic diagram**: when the idea has a mechanism or pipeline, include a simple inline SVG or CSS diagram that shows the transformation, for example `Existing model -> Proposed shift -> Claim test`.
- **Evidence-aware TODOs**: mark missing real-world datasets, baselines, metrics, or results explicitly as `TODO`; do not let visual polish imply completed evidence.
- **Risk ledger**: include a visually distinct section for the strongest reviewer objections and how the claim should be bounded.
- **Next-step ledger**: end with a short priority table or ledger (`P0`, `P1`, `P2`) that tells the user what to implement or validate next.

Use this pattern especially when the user says the output is too plain, too document-like, or should look like a shareable research brief.

## Publication Mode Pattern

When the user asks for a more paper-like, academic, printable, ACM/IEEE-inspired, or publication-grade HTML report, use a publication mode instead of a dashboard-only page.

Required elements:

- **Paper header**: include a title, short subtitle, authors/affiliation placeholders only when provided, abstract, keywords, and contribution summary.
- **Article structure**: use `<article>` as the main container, `<section>` for numbered sections, `<figure>`/`<figcaption>` for diagrams, `<table>`/`<caption>` for experiment plans, and `<div class="equation">` for equations.
- **CSS counters**: number sections, figures, tables, equations, and references with CSS counters when the report reads like a paper draft.
- **Print CSS**: include `@media print` and `@page` rules with a stable page size, margins, monochrome-safe colors, and rules that avoid breaking figures/tables/equations across pages.
- **Two reading modes**: preserve web readability while making print/PDF export clean. Use a single-column article for dense reasoning; use two-column print layout only if tables and equations remain legible.
- **Publication typography**: prefer restrained serif body text or a serif/sans pairing, 65-85 character line lengths, compact headings, clear captions, and no oversized hero typography.
- **Citation scaffolding**: only include real citations if provided. If citations are missing, add a visible `TODO: add related work citations` note rather than fake references.
- **Caption discipline**: every figure/table caption should explain the claim being tested or the evidence it summarizes, not merely name the object.

Use this pattern when the output should support a paper draft, lab memo, thesis note, arXiv-style concept page, or print-to-PDF artifact.

## When to Use Other Skills First

If the research idea is still shallow or unclear, first use research-logic to reconstruct the mechanism-level contribution.

If the experiments are weak or unspecified, first use experiment-design to define research questions, baselines, ablations, metrics, and claim boundaries.

Then use this skill to synthesize both into a single HTML report.

## Required HTML Report Structure

Generate a standalone `.html` file with embedded CSS and minimal embedded JavaScript only when useful. Do not require a build step.

Recommended sections:

1. Hero summary: title, one-sentence claim, status tags.
2. Research motivation: problem, gap, why existing methods are insufficient.
3. Core claim: precise paper claim and claim boundary.
4. Innovation map: 3-5 contribution cards.
5. Method logic: state variables, transition rule, update rule, readout.
6. Shallow vs deep integration: show why this is not module stacking.
7. Experiment design: RQs, datasets, baselines, ablations, metrics.
8. Evidence matrix: what result would support each claim.
9. Failure cases and risks: where the method may fail.
10. Minimum viable plan: next experiments and implementation tasks.

## Visual Design Rules

Use a clean academic dashboard style:

- restrained colors with strong contrast;
- no decorative blobs or generic gradients;
- responsive layout for desktop and mobile;
- cards only for repeated items such as innovations, baselines, ablations, or risks;
- tables for datasets, metrics, and evidence mapping;
- code/math blocks for equations and transition logic;
- a sticky or compact table of contents when the page is long;
- readable typography and enough spacing for dense technical content.
- use 2-4 coordinated semantic colors at most, such as one main accent plus muted warning/evidence colors;
- add visual hierarchy with section labels, status cards, diagrams, and ledgers rather than with decoration;
- make the first viewport immediately signal the research topic, central claim, and evidence maturity.

Prefer semantic HTML:

```html
<header>, <main>, <section>, <article>, <table>, <figure>, <aside>
```

For publication mode, add a compact embedded style pattern like:

```css
article { max-width: 900px; margin: 0 auto; }
section { counter-increment: section; }
section > h2::before { content: counter(section) ". "; }
figure { counter-increment: figure; break-inside: avoid; }
figcaption::before { content: "Figure " counter(figure) ". "; font-weight: 700; }
table { counter-increment: table; break-inside: avoid; }
caption::before { content: "Table " counter(table) ". "; font-weight: 700; }
.equation { counter-increment: equation; break-inside: avoid; }
.equation::after { content: "(" counter(equation) ")"; float: right; }
@page { size: A4; margin: 18mm 16mm; }
@media print { nav, .no-print { display: none; } body { background: #fff; } }
```

Adapt this pattern instead of copying an external stylesheet.

## Content Transformation Rules

### Central Claim

Turn vague text into:

```text
This paper claims that ___ improves/changes ___ because ___.
```

In HTML, place it near the top as a highlighted claim block.

### Innovation Points

Each innovation card should include:

- title;
- mechanism;
- why it is new;
- what experiment validates it.

### Method Logic

Show the model as a sequence:

```text
state after previous event
-> principle-governed evolution
-> state before next event
-> event-induced correction
-> prediction
```

For CTQW dynamic graph ideas, include:

```text
Psi(t_k^-) = exp(-i H(t_{k-1}) Delta t_k) Psi(t_{k-1}^+)
Psi(t_k^+) = EventUpdate(Psi(t_k^-), e_k)
```

### Experiment Plan

Present experiments as tables:

```text
Research Question | Evidence Needed | Dataset | Baseline | Metric | Success Criterion
```

Also include an ablation table:

```text
Variant | What It Tests | Expected Outcome | Claim Supported
```

### Publication Components

When using publication mode, structure the report like:

```text
Title
Abstract
Keywords
1. Introduction / Motivation
2. Method
3. Experimental Design
4. Expected Evidence and Ablations
5. Threats to Validity
6. Minimum Implementation Plan
References or TODO citation ledger
```

Include figures and tables with captions:

```html
<figure id="fig-method">
  <svg><!-- mechanism diagram --></svg>
  <figcaption>Mechanism-level integration of inter-event CTQW evolution and event correction.</figcaption>
</figure>

<table id="tab-ablation">
  <caption>Ablations required to separate CTQW evolution from generic continuous propagation.</caption>
  ...
</table>
```

### Claim Discipline

End the page with explicit claim boundaries:

```text
If results show ___, we can claim ___.
If results show ___, we must weaken the claim to ___.
```

## Output Requirements

When asked to create an HTML report:

1. Choose a clear file path, usually `reports/<topic-name>.html` or `outputs/reports/<topic-name>.html`.
2. Create parent directories if needed.
3. Write a complete standalone HTML file.
4. Use embedded CSS.
5. Avoid external CDN dependencies unless the user explicitly asks.
6. Include no placeholder sections unless marked as TODO with a concrete next action.
7. Include a subtle acknowledgement footer only when the report itself is about HTML generation or when the user asks for acknowledgements; otherwise keep acknowledgements in the skill documentation.
8. After writing, report the file path and summarize what the page contains.
9. If using publication mode, make the file printable without a build step and verify that figures, tables, equations, and citations have meaningful labels or TODOs.

## Quality Checklist

Before finishing, verify:

1. The `<title>` is specific and not a placeholder.
2. The hero states the exact research claim.
3. Every innovation card has a validation path.
4. Every table has meaningful headers and no empty placeholder rows.
5. The page has clear claim boundaries.
6. No section is only decorative.
7. Mobile layout remains readable.
8. Fonts, colors, spacing, and card styles are consistent.
9. There are no unclosed tags or broken anchor links.
10. The final file can open directly in a browser.
11. If using the research brief pattern, the page includes status cards, at least one mechanism diagram, a risk ledger, and a next-step ledger.
12. Any missing evidence is visibly marked as TODO rather than implied as complete.
13. If using publication mode, sections, figures, tables, equations, and references are numbered consistently.
14. Print styles do not hide essential content or split a key figure/table/equation awkwardly.

## Recommended Invocation

```text
Use $research-logic and $experiment-design first, then use $research-html-report to create a standalone HTML page summarizing the paper idea, innovation points, method logic, and experiment plan.
```

## Minimal HTML Skeleton

Use this skeleton as a starting point when useful:

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Research Plan</title>
  <style>
    :root { color-scheme: light; }
    body { margin: 0; font-family: Arial, sans-serif; line-height: 1.6; color: #172033; background: #f7f8fb; }
    main { max-width: 1180px; margin: 0 auto; padding: 32px 20px; }
    section { margin: 28px 0; }
    .panel { background: #fff; border: 1px solid #dde3ee; border-radius: 8px; padding: 20px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; }
    table { width: 100%; border-collapse: collapse; }
    th, td { border-bottom: 1px solid #e2e7f0; padding: 10px; text-align: left; vertical-align: top; }
    code, pre { background: #eef2f7; border-radius: 6px; }
    pre { padding: 14px; overflow: auto; }
  </style>
</head>
<body>
  <main>
    <header></header>
  </main>
</body>
</html>
```

## One-Sentence Summary

This skill turns research reasoning and experiment design into a standalone HTML research brief that makes the paper's claim, mechanism, evidence, and risks easy to inspect.
