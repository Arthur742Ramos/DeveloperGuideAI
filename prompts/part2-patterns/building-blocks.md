# Building Blocks Template

## Purpose

The four fundamental components of effective prompts: Role, Constraints, Examples, Steps. From Chapter 5.

## The Four Building Blocks

### 1. Role

Sets expertise and perspective:

```
You are a [role with specific expertise].

Focus on:
- [aspect 1]
- [aspect 2]
- [aspect 3]
```

**Examples:**
- "You are a senior software engineer reviewing code for production readiness"
- "You are a security auditor looking for vulnerabilities"
- "You are a technical writer explaining concepts to beginners"

### 2. Constraints

Shapes the output format and boundaries:

```
Constraints:
- Return valid [format] only, no extra text
- Maximum [number] words/lines
- Use only [specific tools/libraries]
- Include [required elements]
- Avoid [things to exclude]
```

### 3. Examples

Shows rather than tells:

```
Examples:

Input: "[example input 1]"
Output: "[example output 1]"

Input: "[example input 2]"
Output: "[example output 2]"

Now process: "[actual input]"
```

### 4. Steps

Explicit ordering for complex tasks:

```
Process this in order:

Step 1: [first action] - output: [what to produce]
Step 2: [second action] - output: [what to produce]
Step 3: [third action] - output: [what to produce]

Complete each step before moving to the next.
```

## Combined Template

```
Role: You are a [expertise] who [perspective/priority].

Task: [clear description of what to accomplish]

Context:
- [relevant background 1]
- [relevant background 2]

Constraints:
- [format requirement]
- [length requirement]
- [style requirement]
- [what to avoid]

Examples:
Input: [example]
Output: [example]

Steps:
1. [first step]
2. [second step]
3. [third step]

Begin with step 1.
```

## When to Use Which

| Situation | Building Blocks Needed |
|-----------|------------------------|
| Quick factual question | None (just ask) |
| Simple generation | Constraints (format, length) |
| Style-sensitive output | Role + Examples |
| Multi-step analysis | Steps + Constraints |
| Complex production work | All four |

## Full Example: Code Review

```
Role: You are a senior engineer reviewing code for production deployment.
Prioritize correctness and security over style.

Task: Review this Python function for issues.

Context:
- This handles payment processing
- Called ~1000 times per day
- Must never fail silently

Constraints:
- Return issues as a numbered list
- Include line numbers
- Rate each: CRITICAL / MAJOR / MINOR
- Focus on bugs and security; ignore style

Example:
Input: (function with off-by-one error)
Output:
1. [CRITICAL] Line 15: Off-by-one error in loop bounds.
   The loop processes n+1 items instead of n.
   Fix: Change `range(n+1)` to `range(n)`

Steps:
1. Read the function and understand its purpose
2. Check for logical errors
3. Check for security issues
4. Check for error handling gaps
5. List all issues found

[paste code here]
```
