# Verification Checklist Template

## Purpose

Systematically verify AI outputs before using them. From Chapter 4 on working with uncertainty.

## The Prompt

```
Before I use this output, help me verify it:

1. What assumptions did you make that I should check?
2. What parts are you most/least confident about?
3. What could go wrong if any part is incorrect?
4. What tests or checks would validate this?

For each part of your answer, indicate confidence:
- HIGH: Well-established, widely documented
- MEDIUM: Likely correct but should verify
- LOW: Uncertain, based on inference
```

## Usage Notes

- **When to use**: After receiving any output you plan to use in production
- **Customize**: Add domain-specific verification steps
- **Key insight**: AI cannot truly assess its own uncertainty, but asking surfaces useful caveats

## Verification by Output Type

### Code Verification

```
For the code you just generated:

1. Does it compile/run without errors?
2. What edge cases should I test?
3. What error conditions aren't handled?
4. Are there any security concerns?
5. What dependencies or environment assumptions exist?

List specific tests I should run to validate correctness.
```

### API/Configuration Verification

```
For the API usage / configuration you provided:

1. Which parameter names should I verify against official docs?
2. What version of the API/tool is this for?
3. Are there any deprecated features used?
4. What would break if I'm using a different version?

I will check: [list what you'll verify against]
```

### Factual Claims Verification

```
For the factual claims in your response:

1. Which claims should I verify against primary sources?
2. What's your knowledge cutoff relevant to this topic?
3. Are there any statistics or numbers I should double-check?
4. What sources would you recommend I consult?
```

## Quick Verification Checklist

| Output Type | Verification Method |
|-------------|---------------------|
| Code | Compile, run tests, read it yourself |
| API usage | Check against official documentation |
| Statistics | Verify against authoritative source |
| Configuration | Test in staging first |
| Commands | Dry run with echo before executing |
| Explanations | Cross-check with your domain knowledge |

## Example: Verifying Database Query

```
You suggested this query:
[paste query]

Before I run it:
1. Is this syntax correct for PostgreSQL 15?
2. What indexes would make this efficient?
3. What happens if the table is empty?
4. Could this lock the table or cause performance issues?
5. What's the worst-case execution time on a large table?

I will test on staging with EXPLAIN ANALYZE before production.
```
