# Debugging Assistant Template

## Purpose

Structured debugging assistance for complex issues. From Chapter 11.

## The Prompt

```
You are my debugging assistant.

Problem: [describe symptom in 2-3 sentences]

Context:
- Tech stack: [e.g., Python service, PostgreSQL, Kubernetes]
- Environment: [dev/staging/prod, relevant constraints]
- What I've already tried:
  - [attempt 1]
  - [attempt 2]

Relevant information:
```
[paste error message, logs, config, or code]
```

Your tasks:
1. Restate the problem in your own words
2. List 3-5 plausible hypotheses, ranked by likelihood
3. For each hypothesis: what evidence would support or refute it
4. Propose specific checks (commands, queries, experiments) for top hypotheses
5. Suggest likely fix, clearly marking assumptions

Constraints:
- If something depends on version or environment, state assumptions
- Separate "high confidence" suggestions from speculative ones
- If you need more information, ask specific questions
```

## Follow-Up After Running Checks

```
Here are the results of the checks you suggested:

[paste results]

Given this new data:
1. Which hypothesis is most likely now?
2. What's the concrete fix or mitigation?
3. Any long-term improvements to prevent recurrence?
```

## Quick Debug (Simple Issues)

```
Error: [paste error message]

Code that triggered it:
```[language]
[paste code]
```

What's wrong and how do I fix it?
```

## Systematic Debug (Complex Issues)

```
I'm debugging a complex issue. Help me be systematic.

Symptom: [what's happening]
Expected: [what should happen]
Environment: [where this occurs]

Let's work through this:

1. First, what information do you need to form hypotheses?
2. [I provide info]
3. What are your hypotheses?
4. What should I check first?
5. [I report results]
6. What next?

Guide me through the investigation step by step.
```

## Log Analysis

```
Help me analyze these logs to find the problem.

Context: [what the system does, what failed]

Logs:
```
[paste relevant logs]
```

Please:
1. Identify any errors or warnings
2. Trace the sequence of events
3. Note anything unusual in timing or order
4. Suggest what to investigate further
```

## Query Generation for Debugging

```
I need to find [what you're looking for] in our [database/logs].

Schema/format:
- [relevant schema or log format]

Help me write a query that:
1. Filters to relevant records
2. Groups/aggregates usefully
3. Orders by most likely to be relevant

Explain what each part of the query does.
```

## Runbook Generation (Post-Debug)

```
We just debugged an issue where [brief description].

Root cause: [explanation]

Write a runbook for future on-call engineers:

1. How to recognize this problem
2. Step-by-step diagnosis commands
3. The fix, with safety checks
4. How to verify the fix worked
5. When to escalate instead

Keep it concise and copy-paste friendly.
```

## Common Debugging Questions

```
# Network issues
What could cause intermittent connection timeouts to [service]?

# Memory issues
The service memory keeps growing. What should I check?

# Performance issues
This query is slow. What indexes might help?

# Race conditions
This works locally but fails in CI. What timing issues should I look for?
```
