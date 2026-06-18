# Research Logic Skill: From Connection Discovery to Essential Integration

## Purpose

This skill guides a research reasoning process for turning a possible combination of two methods into a deeper, mechanism-level or principle-level integration.

It is not a skill for building one specific model. Instead, it helps the user move through the following path:

\[
\boxed{
\text{discover a connection point}
\rightarrow
\text{try a direct integration}
\rightarrow
\text{diagnose shallow fusion}
\rightarrow
\text{return to the underlying principle}
\rightarrow
\text{reconstruct the model logic}
}
\]

Use QWTA + TGN only as an example when helpful. Do not present "Hamiltonian QW-TGN" as the skill itself. The skill is a general research-thinking framework.

---

## When to Use This Skill

Use this skill when the user asks how to:

1. Combine two research ideas, models, theories, or mechanisms.
2. Decide whether a proposed combination is meaningful or only a module-level patch.
3. Find the true mechanism-level connection between two methods.
4. Transform a direct engineering fusion into a more principled formulation.
5. Build a clear research narrative from initial intuition to theoretical reconstruction.
6. Explain why a model integration is not merely "A + B" but changes the underlying state, dynamics, or assumptions of one method.

Example domains include, but are not limited to:

- QWTA + TGN;
- quantum walks + dynamic graph neural networks;
- physics-inspired models + deep learning architectures;
- continuous-time dynamics + event-driven neural systems;
- graph neural networks + differential equations;
- neural memory models + physical evolution operators.

---

## Core Rule

Always distinguish three levels of integration:

### Level 1: Modular Fusion

One method is inserted into another method as a replaceable block.

\[
\text{Model A module} \rightarrow \text{Model B block} \rightarrow \text{output}
\]

This is useful but often shallow.

### Level 2: Mechanistic Fusion

One method changes how the internal mechanism of the other method operates.

\[
\text{internal state} \rightarrow \text{new mechanism-driven transition} \rightarrow \text{updated state}
\]

This is usually the most practical target for a strong paper.

### Level 3: Principle-Level Reconstruction

One method's fundamental principle rewrites the core assumption of the other method.

\[
\text{old assumption} \Rightarrow \text{new principle-governed formulation}
\]

This is the deepest form of integration, but it usually requires stronger mathematical and experimental support.

---

## Main Reasoning Workflow

### Stage 1: Identify the Native Function of Each Method

Do not begin by asking where to insert one method into another. Begin by asking what each method fundamentally does.

For each method, identify:

1. Its input and output.
2. Its core internal state.
3. Its update or propagation rule.
4. Its central mathematical object.
5. The problem it was originally designed to solve.
6. The assumption it makes about the world.

Use this template:

```text
Method A solves: ...
Method A's state is: ...
Method A's transition rule is: ...
Method A's key mathematical object is: ...

Method B solves: ...
Method B's state is: ...
Method B's transition rule is: ...
Method B's key mathematical object is: ...
```

Then infer the first possible connection point.

---

### Stage 2: Find the First Direct Connection Point

The first connection point usually appears at an interface:

- input representation;
- message function;
- aggregation layer;
- memory state;
- transition rule;
- embedding module;
- decoder;
- loss function;
- physical operator;
- latent dynamics.

At this stage, propose the most direct integration without overclaiming.

Use this sentence pattern:

```text
The first natural connection is that Method A provides ___, while Method B needs ___ at the level of ___.
```

For example:

```text
The first natural connection is that QWTA provides continuous-time graph propagation, while TGN needs a graph-based embedding module for temporal node memories.
```

---

### Stage 3: Build the Shallow Version First

Construct the simplest valid fusion. This is not the final contribution; it is a diagnostic baseline.

A shallow version is valuable because it clarifies:

1. where the two models can technically connect;
2. what the minimal implementation looks like;
3. what is still unsatisfactory;
4. which part of the original model remains unchanged.

Write the shallow version explicitly.

Example:

\[
\text{TGN memory}
\rightarrow
\text{QWTA embedding}
\rightarrow
\text{decoder}
\]

This is a valid design, but it should not be treated as the deepest contribution.

---

### Stage 4: Diagnose Whether the Fusion Is Shallow

Ask the critical question:

```text
Does the inserted method change the host model's core assumption, or does it only replace one module?
```

A fusion is probably shallow if:

1. the original state update of the host model is unchanged;
2. the new method appears only after the main state has already been formed;
3. the new method can be replaced by attention, MLP, GCN, or sum aggregation without changing the conceptual story;
4. the explanation says only "we use A to enhance B";
5. the claimed mechanism is not tied to a precise mathematical operator or state transition.

Use this warning sentence:

```text
At this stage, the combination is technically valid, but it still treats Method A as a replaceable module rather than as a mechanism that changes Method B's internal logic.
```

---

### Stage 5: Return to the Essence of the Added Method

Now ask what the added method is fundamentally about.

Do not ask:

```text
Where can I insert this module?
```

Ask instead:

```text
What is the mathematical or physical principle that makes this method different?
```

Identify the principle in one sentence.

Example:

```text
QWTA is not fundamentally a neighbor aggregation layer; it is a continuous-time Hamiltonian evolution operator of the form e^{-iH\Delta t}.
```

This sentence becomes the pivot from shallow fusion to essential integration.

---

### Stage 6: Return to the Weak Point of the Host Method

A deep integration becomes convincing when the essence of the added method addresses a structural weakness of the host method.

Ask:

1. What assumption in the host method feels limited?
2. What does the host method fail to model naturally?
3. Where does the host method use an engineering workaround?
4. Can the added method replace that workaround with a more principled mechanism?

Example:

```text
TGN updates node memory only when an event occurs. If a node is inactive for a long time, its memory can become stale. TGN then uses an embedding module to compensate by aggregating neighbor information. This is useful, but it does not define an intrinsic evolution law for inactive memories.
```

This reveals the deeper target:

```text
Use QWTA not merely to aggregate memory after the fact, but to define how memory evolves between events.
```

---

### Stage 7: Reconstruct the Model Around the Essential Principle

Now rewrite the model logic so that the added method changes the internal state transition of the host model.

Use the pattern:

\[
\text{state before interval}
\rightarrow
\text{principle-governed evolution}
\rightarrow
\text{state before event}
\rightarrow
\text{event-induced update}
\rightarrow
\text{state after event}
\]

For the QWTA + TGN example:

\[
\Psi(t_{k-1}^{+})
\xrightarrow{\ e^{-iH\Delta t_k}\ }
\Psi(t_k^{-})
\xrightarrow{\ \text{event update}\ }
\Psi(t_k^{+})
\]

This changes the interpretation from:

\[
\text{event-triggered memory update only}
\]

to:

\[
\boxed{
\text{continuous inter-event evolution} + \text{event-induced local correction}
}
\]

This is the essential integration.

---

### Stage 8: Explain the New Research Logic

The final explanation should not sound like module stacking.

Avoid:

```text
We combine QWTA and TGN to improve performance.
```

Prefer:

```text
We first identify that TGN provides event-driven memory while QWTA provides continuous-time graph evolution. A direct fusion places QWTA in the embedding module, but this only uses QWTA as an aggregation operator. Returning to the physical meaning of QWTA, we reinterpret its operator e^{-iH\Delta t} as an inter-event memory evolution law. Thus, the dynamic graph is no longer modeled only as discrete event-triggered memory updates, but as a state system that evolves continuously between events and is locally perturbed when events occur.
```

---

## Socratic Checkpoints

Ask these questions before finalizing the integration:

1. What is the first obvious connection point?
2. Is that connection only an interface-level match?
3. What core assumption of the host model remains unchanged?
4. What is the mathematical essence of the inserted method?
5. Does the inserted method change a state transition, or only a representation?
6. Can the method still be explained if the inserted block is replaced by attention or an MLP?
7. What problem of the host method does the inserted method solve at a mechanistic level?
8. What is the new state variable after reconstruction?
9. What is the new transition rule?
10. What should be claimed modestly, and what can be claimed as the true contribution?

---

## Devil's Advocate Tests

### Test 1: Replaceability Test

If the inserted method can be replaced by a generic neural layer without changing the research story, the integration is shallow.

### Test 2: State-Dynamics Test

If the internal state dynamics of the host model are unchanged, the integration is probably modular, not essential.

### Test 3: Principle Test

If the explanation does not identify the mathematical principle of the inserted method, the contribution is under-theorized.

### Test 4: Host-Weakness Test

If the added method does not address a specific weakness or limitation of the host method, the integration may lack necessity.

### Test 5: Overclaim Test

Do not claim principle-level integration if the actual implementation only uses a method as a plug-in layer.

---

## Failure Modes and Recovery Strategies

### Failure Mode 1: The integration becomes simple module stacking

Symptom:

```text
Method A output -> Method B layer -> prediction
```

Recovery:

- identify the host model's core state;
- move the added method into the state transition;
- define how the state changes before and after the added method acts.

---

### Failure Mode 2: The theoretical explanation is only metaphorical

Symptom:

```text
The model is inspired by physics.
```

but no operator, state, or equation is defined.

Recovery:

- define the state variable;
- define the operator;
- define the transition equation;
- define how events or inputs modify the state or operator.

---

### Failure Mode 3: The deepest version is too hard to implement

Symptom:

The model requires expensive dynamic operators, repeated eigendecompositions, or unstable training.

Recovery:

- implement the mechanism-level version first;
- use fixed or slowly updated operators;
- treat the full principle-level version as an extension;
- report the gap honestly.

---

### Failure Mode 4: The example becomes mistaken for the skill itself

Symptom:

The skill is named after one application, such as "Hamiltonian QW-TGN", even though the intended skill is a general research reasoning method.

Recovery:

- rename the skill around the reasoning logic;
- move the specific model into an application example;
- describe the reusable pattern separately from the domain case.

---

## Application Example: QWTA + TGN

This example illustrates the skill. It is not the skill itself.

### Step 1: Discover the connection point

TGN provides event-driven node memories:

\[
s_i(t)
\]

QWTA provides continuous-time graph evolution:

\[
U(\Delta t)=e^{-iH\Delta t}
\]

The first connection is:

\[
\text{TGN memory} + \text{QWTA graph propagation}
\]

---

### Step 2: Try the direct integration

Use QWTA as a TGN embedding module:

\[
S(t)=[s_1(t),\dots,s_N(t)]^\top
\]

\[
Z(t)=\operatorname{QWTAEmb}(S(t),L,\Delta t)
\]

This is valid but shallow.

---

### Step 3: Diagnose the shallow part

If QWTA only appears after TGN memory is already updated, then QWTA is acting as an aggregation or embedding layer.

The original TGN memory dynamics are still unchanged.

---

### Step 4: Return to QWTA's essence

QWTA is fundamentally:

\[
\Psi(t+\Delta t)=e^{-iH\Delta t}\Psi(t)
\]

It is not merely neighbor aggregation.

---

### Step 5: Return to TGN's weakness

TGN memory is updated only when events occur. Inactive nodes may have stale memory.

This suggests a deeper integration:

\[
\text{Use QWTA to evolve memory between events.}
\]

---

### Step 6: Reconstruct the model

Define complex-valued node memory:

\[
\Psi(t)\in\mathbb{C}^{N\times d}
\]

Inter-event evolution:

\[
\Psi(t_k^-)=e^{-iH\Delta t_k}\Psi(t_{k-1}^+)
\]

Event-induced update:

\[
\Psi(t_k^+)=\operatorname{EventUpdate}(\Psi(t_k^-),x(t_k))
\]

Readout:

\[
Z(t_k)=\operatorname{Readout}(\Psi(t_k^+))
\]

This is the essential integration.

---

## Recommended Output Pattern

When applying this skill, respond in the following order:

1. **Native functions**: explain what each method originally does.
2. **First connection**: identify the direct interface-level connection.
3. **Shallow attempt**: write the simplest valid integration.
4. **Critical diagnosis**: explain why this may be shallow.
5. **Essence return**: identify the deeper principle of the inserted method.
6. **Host weakness**: identify what limitation of the host method this principle can address.
7. **Essential reconstruction**: rewrite the state transition or model logic.
8. **Claim discipline**: distinguish what is implemented now from what is a future extension.

---

## Claim Discipline

Use cautious and precise language.

Say:

```text
This formulation moves the integration from a module-level embedding replacement toward a mechanism-level state-evolution design.
```

Avoid:

```text
This fully solves dynamic graph learning through quantum mechanics.
```

Say:

```text
The physical interpretation is grounded in the explicit operator e^{-iH\Delta t}, provided that the state, Hamiltonian, and event update are clearly defined.
```

Avoid:

```text
The model is quantum because it uses complex numbers.
```

---

## Minimal Invocation Prompt

```text
Use the Research Logic Skill: From Connection Discovery to Essential Integration. Help me analyze how two methods can be combined. First identify the direct connection point, then build the shallow integration, then challenge whether it is merely modular, and finally reconstruct a deeper mechanism-level or principle-level integration.
```

---

## One-Sentence Summary

\[
\boxed{
\text{A deep research integration does not merely insert one method into another; it uses one method's core principle to rewrite the other's internal logic.}
}
\]
