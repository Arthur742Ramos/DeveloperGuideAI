# Complete Prompt Reference

All prompt templates in one document. Copy and adapt for your use.

---

## Part 1: Foundations

### Contract-Style Prompt

```
Task: [describe in 1-2 sentences]

Context:
- Domain: [web development, data analysis, etc.]
- Environment: [tools, frameworks, constraints]
- Target audience: [who uses this output]

Input I will provide:
- [code, data, error messages, etc.]

Output I want:
- [format: code + explanation, bullets, etc.]

Process:
1. Ask clarifying questions if needed (max 5)
2. Propose a brief plan
3. Execute step by step

Begin with step 1.
```

### Verification Checklist

```
Review this output before I use it:

[paste AI output]

Check:
1. Does it actually do what I asked?
2. Are there obvious errors or bugs?
3. Does it handle edge cases I care about?
4. Are there security issues?
5. Does it match my codebase style?

Be critical. I need honest assessment.
```

### Conversation Management

```
# Reset context
Let's start fresh. Here's what I need:
[new task description]
Ignore our previous discussion.

# Summarize progress
Summarize what we've accomplished so far and what remains.

# Branch exploration
Set aside our current approach. Let's explore an alternative:
[alternative approach]
We can come back to the original if this doesn't work.
```

### Uncertainty Signals

```
For this response, rate your confidence:
- HIGH: Standard pattern, well-documented
- MEDIUM: Likely correct, should verify
- LOW: Uncertain, making assumptions

Flag any parts where you're guessing or making assumptions I should check.
```

---

## Part 2: Core Patterns

### Building Blocks Template

```
Role: You are a [expertise] focused on [specific aspect].

Task: [what to do]

Constraints:
- [format constraint]
- [length constraint]
- [style constraint]
- [technical constraint]

Example of desired output:
[show one example]

Steps:
1. [first step]
2. [second step]
3. [third step]

Input:
[paste input here]
```

### Clarify-Plan-Execute

```
# Phase 1: Clarify
Before starting, I need to understand:
1. [question about requirements]
2. [question about constraints]
3. [question about context]

# Phase 2: Plan
Based on the answers, here's my proposed approach:
1. [step 1]
2. [step 2]
3. [step 3]

Does this plan look right? Any adjustments?

# Phase 3: Execute
[proceed with approved plan]
```

### Code Review

```
You are a senior engineer reviewing code for production.

Language: [language]
Context: [what this code does]

```[language]
[paste code]
```

Evaluate:
1. Correctness: Does it work?
2. Error handling: Failures covered?
3. Performance: Obvious issues?
4. Readability: Clear to others?
5. Security: Vulnerabilities?

For each: GOOD / NEEDS WORK / PROBLEM
Include line numbers and specific fixes.
```

### Security Review

```
Review as a security auditor:

```[language]
[code]
```

Check for:
1. Input validation (SQLi, XSS, command injection)
2. Auth/authz flaws
3. Sensitive data exposure
4. Crypto issues
5. OWASP Top 10

For each finding: Severity, location, attack vector, fix.
```

### Review Loop

```
# Generate
[initial generation prompt]

# Review
Review what you just produced:
- What's good?
- What's weak?
- What's missing?

# Revise
Based on your review, produce an improved version.
Focus on: [specific improvement areas]
```

### Multi-Role Workflow

```
# Architect Role
Design the approach for: [task]
Consider: trade-offs, alternatives, risks
Output: Design document with key decisions

# Coder Role
Implement the design above.
Focus on working code. We'll review separately.

# Tester Role
Generate tests for the implementation:
- Normal cases
- Edge cases
- Error cases

# Reviewer Role
Review the code against the original design.
Note any deviations or concerns.
```

### ReAct Pattern

```
You have access to these tools:
- search(query): Search documentation
- read_file(path): Read file contents
- run_command(cmd): Execute shell command

For each step:
1. Thought: What do I need to find out?
2. Action: Which tool to use and how
3. Observation: What did I learn?
4. Repeat until solved

Task: [what to investigate or accomplish]
```

---

## Part 3: Workflows

### Code Generation

```
Language: [language and version]
Style: [conventions]
Dependencies: [allowed/prohibited]

Task: [what to implement]

Requirements:
- [requirement 1]
- [requirement 2]

Context:
- Used in: [where/how]
- Similar code: [patterns to follow]

Output: Implementation + explanation + assumptions to verify
```

### Refactoring

```
Goal: [what to improve]

Current code:
```[language]
[paste code]
```

Constraints:
- Keep public API identical
- Don't change behavior
- [specific constraints]

First explain approach, then show refactored code.
```

### Debugging

```
Problem: [symptom in 2-3 sentences]

Context:
- Stack: [languages, frameworks, infra]
- Environment: [dev/staging/prod]
- Already tried: [attempts]

```
[error message, logs, or code]
```

Tasks:
1. Restate the problem
2. List 3-5 hypotheses by likelihood
3. Evidence that would confirm/refute each
4. Specific checks for top hypotheses
5. Likely fix with assumptions marked
```

### Test Generation

```
Generate tests for:

```[language]
[paste function]
```

Cover:
1. Normal operation (3-5 cases)
2. Edge cases: empty, single, large, boundary, unicode
3. Error cases: wrong types, null, out-of-range

For each test: descriptive name, clear assertion, comment on why it matters.
```

### Log Analysis

```
Analyze these logs to find the problem:

Context: [what failed]

```
[paste logs]
```

Please:
1. Identify errors/warnings
2. Trace event sequence
3. Note unusual timing/order
4. Suggest what to investigate
```

### Paper Summary

```
Summarize this paper for a practitioner:

[paste abstract or key sections]

Provide:
1. Main contribution (2-3 sentences)
2. Key techniques used
3. Results and limitations
4. Practical takeaways
5. Questions I should investigate further

Flag claims you cannot verify from the excerpt.
```

### MVP Scoping

```
Idea: [brief description]

Questions to clarify:
1. Who is the user?
2. What problem does this solve?
3. How do they solve it today?
4. What's the simplest thing that would help?

Once answered, help me define:
- Core feature (one thing it must do)
- Out of scope for v1
- Success metric
- Tech approach (simplest that works)
```

### Runbook Generation

```
We debugged: [brief description]
Root cause: [explanation]

Write a runbook for on-call:
1. How to recognize this problem
2. Step-by-step diagnosis commands
3. The fix with safety checks
4. How to verify fix worked
5. When to escalate

Keep it concise and copy-paste friendly.
```

---

## Part 4: Safety and Evaluation

### Data Anonymization

```
I need to share this data with AI but it contains sensitive info:

[paste sample]

Help me:
1. Identify all PII/sensitive fields
2. Suggest anonymization for each
3. Show anonymized version
4. Note what context is lost

Goal: Remove identifying info while keeping the problem solvable.
```

### Before Sharing Checklist

```
Review this before I paste it into AI:

[paste content]

Flag if it contains:
- [ ] Credentials or API keys
- [ ] Personal information (names, emails, etc.)
- [ ] Internal URLs or IPs
- [ ] Proprietary business logic
- [ ] Customer data
- [ ] Security vulnerabilities that shouldn't be shared

Suggest redactions if needed.
```

### Evaluating AI Assistance

```
I just used AI for: [task]

Evaluate honestly:
- Time spent prompting: [X minutes]
- Time fixing output: [X minutes]
- Estimated time without AI: [X minutes]

Was this a win?
What would I do differently next time?
```

---

## Part 5: Tool Configuration

### CLAUDE.md Template

```markdown
# Project: [Name]

## Commands
- `[build command]`
- `[test command]`
- `[lint command]`

## Structure
- src/routes/ - HTTP handlers
- src/services/ - Business logic
- src/repositories/ - Database access

## Conventions
- [convention 1]
- [convention 2]
- Pattern example: src/services/userService.ts

## Do Not
- Modify [generated files]
- Commit [sensitive files]
- [other constraints]
```

### AGENTS.md Template

```markdown
# [Project Name]

## Quick Start
```bash
[install command]
[dev command]
[test command]
```

## Architecture
- [component]: [location and purpose]
- [component]: [location and purpose]

## Standards
- [standard 1]
- [standard 2]

## Do Not
- [constraint 1]
- [constraint 2]
```

### copilot-instructions.md Template

```markdown
# [Project Name]

## Tech Stack
- [language] [version]
- [framework] [version]

## Code Style
- [style guide reference]
- [naming conventions]

## Patterns
- [pattern]: see [file] for example
- [pattern]: see [file] for example

## Forbidden
- [thing to avoid]
- [thing to avoid]
```

### MCP Tool Design

```
Design an MCP tool for: [purpose]

Requirements:
- Single responsibility
- Clear input/output types
- Graceful error handling

Provide:
1. Tool name and description (for AI to understand when to use it)
2. Input schema
3. Output format
4. Error cases and responses
5. Example usage
```

---

## Quick Patterns

### Explain Code
```
Explain this code as if to a developer who needs to modify it:
```[language]
[code]
```
Cover: purpose, main steps, non-obvious parts, modification risks.
```

### Fix This Error
```
Error: [paste error]
Code: [paste relevant code]
What's wrong and how do I fix it?
```

### Write Documentation
```
Write documentation for:
```[language]
[code]
```
Include: description, parameters, return value, example usage.
```

### Suggest Improvements
```
Review this code and suggest improvements:
```[language]
[code]
```
Focus on: [readability/performance/security/maintainability]
```
