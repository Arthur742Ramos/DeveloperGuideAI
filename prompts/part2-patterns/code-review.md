# Code Review Template

## Purpose

Structured code review for production readiness. From Chapters 5 and 7.

## The Prompt

```
You are a senior engineer reviewing this code for production readiness.

Language: [language]
Context: [what this code does, where it runs]

```[language]
[paste code here]
```

Evaluate against these criteria:

1. **Correctness**: Does it do what it claims?
2. **Error handling**: Are failure cases covered?
3. **Performance**: Any obvious inefficiencies?
4. **Readability**: Could a new team member understand this?
5. **Security**: Any potential vulnerabilities?

For each criterion:
- Rating: GOOD / NEEDS WORK / PROBLEM
- Specific feedback with line numbers
- Suggested fix if applicable

Be direct about issues. I need honest assessment, not encouragement.
```

## Usage Notes

- **Customize criteria**: Add/remove based on what matters for your codebase
- **Provide context**: More context about usage patterns improves review quality
- **Verify findings**: Always manually verify issues the AI identifies

## Variations

### Security-Focused Review

```
Review this code as a security auditor.

Focus on:
1. Input validation (SQL injection, XSS, command injection)
2. Authentication/authorization flaws
3. Sensitive data exposure
4. Cryptographic issues
5. OWASP Top 10 vulnerabilities

For each finding:
- Severity: CRITICAL / HIGH / MEDIUM / LOW
- Location (line number)
- Attack vector
- Remediation

```[language]
[code]
```
```

### Performance Review

```
Review this code for performance issues.

Context:
- Expected load: [requests/records per second]
- Data size: [typical and maximum]
- Environment: [constraints]

Check for:
1. Algorithmic complexity issues
2. Unnecessary allocations
3. Missing caching opportunities
4. N+1 query patterns
5. Blocking operations that should be async

For each issue, estimate impact and suggest optimization.
```

### Maintainability Review

```
Review this code from a maintainability perspective.

Assume a new developer will inherit this code.

Check for:
1. Naming clarity
2. Function/method size
3. Documentation gaps
4. Magic numbers or unexplained logic
5. Test coverage opportunities
6. Coupling and cohesion

Focus on what would confuse someone unfamiliar with the codebase.
```

## Multi-Pass Review

For critical code, run multiple focused reviews:

```
# Pass 1: Correctness
Review for logical errors only. Does it do what it should?

# Pass 2: Security
Review for security vulnerabilities only.

# Pass 3: Edge cases
What inputs would break this? What assumptions might be violated?
```

## Post-Review Verification

After the AI review, always:

1. Read the code yourself
2. Verify that identified issues are real
3. Check that suggested fixes don't introduce new problems
4. Run tests after any changes
