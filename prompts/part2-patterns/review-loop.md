# Review Loop Template

## Purpose

The Generate-Review-Revise cycle for improving AI outputs. From Chapter 7.

## The Pattern

```
┌─────────────┐
│  Generate   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Review    │
└──────┬──────┘
       │
       ▼
┌─────────────┐     ┌──────┐
│   Revise    │────▶│ Done │
└──────┬──────┘     └──────┘
       │
       └──────▶ (back to Review if needed)
```

## Step 1: Generate

```
[Your generation prompt - be clear about what you want]

This is a first draft—focus on getting the structure right, not perfection.
```

## Step 2: Review

```
Now review your output against these criteria:

1. [Criterion 1]: [what good looks like]
2. [Criterion 2]: [what good looks like]
3. [Criterion 3]: [what good looks like]

For each criterion:
- Rating: GOOD / NEEDS WORK / PROBLEM
- Specific issues to fix
- What's missing

Be critical. I need honest assessment.
```

## Step 3: Revise

```
Address the issues you identified:

- Fix [issue 1]
- Fix [issue 2]
- Keep [what's working]

Show me the revised version.
```

## Review Criteria by Output Type

### Code Review Criteria

```
Review the code against:

1. Correctness: Does it do what it should?
2. Error handling: Are failures covered?
3. Edge cases: What inputs would break it?
4. Readability: Is intent clear?
5. Security: Any vulnerabilities?
```

### Writing Review Criteria

```
Review this text for:

1. Clarity: Is each sentence unambiguous?
2. Structure: Does the argument flow logically?
3. Evidence: Are claims supported?
4. Conciseness: Can anything be cut without losing meaning?
5. Audience fit: Is it appropriate for [target reader]?
```

### Documentation Review Criteria

```
Review this documentation for:

1. Accuracy: Does it match actual behavior?
2. Completeness: Are all features covered?
3. Examples: Are there enough working examples?
4. Navigation: Can readers find what they need?
5. Freshness: Any outdated information?
```

### Test Review Criteria

```
Review these tests for:

1. Coverage: Are happy paths tested?
2. Edge cases: Are boundaries tested?
3. Error cases: Are failures tested?
4. Isolation: Do tests depend on each other?
5. Clarity: Is each test's purpose obvious?
```

## Knowing When to Stop

- **Round 1**: Usually catches major structural issues
- **Round 2**: Catches edge cases and polish
- **Round 3**: Rarely worth it

If you're on round 4+, the problem is likely underspecified. Go back to clarify requirements.

## Example: Email Draft

### Generate

```
Draft an email to the engineering team announcing the new deployment process.

Key points:
- New process starts Monday
- Main changes: [list changes]
- Where to find documentation
- Who to contact with questions
```

### Review

```
Review this email for:

1. Clarity: Will everyone understand what's changing?
2. Completeness: Are all key points covered?
3. Tone: Is it appropriate for a team announcement?
4. Action items: Is it clear what people need to do?
5. Length: Is it concise enough to be read?

List specific improvements.
```

### Revise

```
Revise based on review:
- Make [section] clearer
- Add [missing information]
- Cut [unnecessary content]
- Keep the [good parts]
```
