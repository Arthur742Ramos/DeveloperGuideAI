# Contract-Style Prompt Template

## Purpose

Structure any AI request as a clear contract with explicit inputs, outputs, and constraints. This is the foundation pattern from Chapter 1.

## The Prompt

```
Task: [Describe the task in 1-2 sentences]

Context:
- Domain: [e.g., web development, data analysis, infrastructure]
- Environment: [tools, frameworks, constraints]
- Target audience: [who will use this output]

Input I will provide:
- [list inputs: code, data, error messages, etc.]

Output I want:
- [format: code + explanation, bullet points, JSON, etc.]
- [length constraints if any]

Constraints:
- [what to include]
- [what to avoid]
- [style requirements]

Process:
1. Ask clarifying questions if needed (max 5)
2. Propose a brief plan
3. Execute step by step

Begin with step 1.
```

## Usage Notes

- **When to use**: Any non-trivial request where you need predictable output
- **Customize**: Remove sections that don't apply; add domain-specific constraints
- **Verify**: Check that output matches the specified format and constraints

## Variations

### Minimal Version (Quick Tasks)

```
Task: [one sentence]

Output: [format]

Constraints:
- [key constraint 1]
- [key constraint 2]
```

### Extended Version (Complex Tasks)

Add these sections:

```
Background:
[2-3 sentences of relevant context the AI needs]

Success criteria:
- [how I'll know this is correct]
- [what "done" looks like]

Anti-patterns to avoid:
- [common mistakes for this task type]
```

## Example: Code Review

```
Task: Review this Python function for production readiness.

Context:
- Domain: Backend API for financial services
- Environment: Python 3.11, FastAPI, PostgreSQL
- Target audience: Senior engineer reviewing before merge

Input I will provide:
- The function code
- Brief description of what it should do

Output I want:
- List of issues (severity: HIGH/MEDIUM/LOW)
- For each: location, problem, suggested fix
- Overall assessment (approve/request changes)

Constraints:
- Focus on correctness, security, and error handling
- Ignore style issues (we have linters for that)
- Be specific about line numbers

Process:
1. Confirm you understand what the function should do
2. Review systematically
3. Provide structured feedback
```
