# Uncertainty Signals Template

## Purpose

Request explicit uncertainty indicators from AI to identify what needs verification. From Chapter 4.

## The Prompt

```
For each part of your answer, indicate your confidence level:

- HIGH: Well-established, widely documented, you've seen many examples
- MEDIUM: Likely correct but should be verified
- LOW: Uncertain, based on inference or extrapolation

Also flag:
- Any assumptions I should verify
- Parts where documentation might have changed since your training
- Areas where my specific context might invalidate your answer
```

## Usage Notes

- **Key insight**: AI cannot truly assess its own uncertainty, but this prompt surfaces useful caveats
- **When to use**: Any factual claims, API usage, configuration advice
- **What to verify**: Anything marked MEDIUM or LOW, plus any HIGH claims in critical areas

## Variations

### For Technical Advice

```
For the technical recommendation above:

Rate your confidence (HIGH/MEDIUM/LOW) on:
1. The approach being correct for my use case
2. The specific syntax/API calls being accurate
3. This working with my stated versions
4. No security issues with this approach

What would you recommend I verify before implementing?
```

### For Code Generation

```
For the code you just generated:

1. What parts are you confident will work as-is?
2. What parts might need adjustment for my environment?
3. What edge cases might this not handle?
4. What assumptions about my codebase are baked in?
```

### For Factual Claims

```
You made several factual claims. For each:

1. [Claim 1] - Confidence? Source I should check?
2. [Claim 2] - Confidence? Source I should check?
3. [Claim 3] - Confidence? Source I should check?

Which of these are most likely to be outdated or context-dependent?
```

## Generating Alternatives for Triangulation

When uncertainty is high, generate multiple approaches:

```
You suggested approach X. Before I commit to it:

1. What are two other ways to solve this problem?
2. What are the tradeoffs between all three approaches?
3. Under what circumstances would each approach be best?
4. Which approach has the most reliable implementation path?
```

## Requesting Self-Critique

```
Before I implement this solution, play devil's advocate:

- What could go wrong with this approach?
- What assumptions are we making that might be false?
- What edge cases might break this?
- If this fails in production, what's the most likely cause?
```
