# Conversation Management Prompts

## Purpose

Manage long or complex AI conversations effectively. From Chapter 3 on iterative dialogue.

## Reset Prompt

Use when a conversation has become confused or gone in an unproductive direction.

```
Let me restart. Here is the core problem:

[Paste essential context - 2-5 sentences max]

Forget our previous attempts. What is the simplest approach to solving this?
```

## Summarize Prompt

Use to clarify state mid-conversation or before continuing.

```
Before we continue, summarize what we have established so far:

1. What is the problem we are solving?
2. What approaches have we tried?
3. What have we learned from each attempt?
4. What are the remaining open questions?

Keep each point to 1-2 sentences.
```

## Branch Prompt

Use when exploring multiple options to keep branches separate.

```
Let's explore [Option A: description] in depth.

We will consider [Option B: description] separately afterward.

For now, focus only on Option A:
- What are the tradeoffs?
- What are the implementation details?
- What could go wrong?
```

## Progress Check Prompt

Use every 5-10 exchanges to ensure you're on track.

```
Quick check: Are we still solving the original problem?

Original goal: [restate it]
Current direction: [what we're discussing now]

If we've drifted, let's refocus. If this tangent is valuable, let's note where to return.
```

## Micro Prompts for Any Conversation

### Summarize Where We Are

```
Summarize in 5-7 bullet points:
- What we've done so far
- What assumptions you're using
- What the next two possible steps are
```

### Critique Your Own Answer

```
Switch to reviewer mode and critique your previous answer:
- 3 things that might be wrong or suboptimal
- 3 ways to make it more robust
```

### Generate Tests and Checks

```
For the solution above, propose:
- Unit tests or scenarios that would validate it
- Queries or checks to confirm it works in production
```

### Make It Production-Grade

```
Take the draft above and refine it for production:
- Error handling
- Edge cases
- Logging and observability
- Comments where logic is non-obvious
```

### Small, Safe Delta

```
Propose the smallest change that moves us toward the goal while minimizing risk.
Explain why it's safer than a bigger change.
```

## When to Use Each

| Situation | Prompt to Use |
|-----------|---------------|
| Conversation is confused | Reset |
| Lost track of progress | Summarize |
| Multiple valid approaches | Branch |
| Been going for 10+ exchanges | Progress Check |
| Need to validate output | Critique Your Own Answer |
| Draft is rough | Make It Production-Grade |
| Risk-averse environment | Small, Safe Delta |
