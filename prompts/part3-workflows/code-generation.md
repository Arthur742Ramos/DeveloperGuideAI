# Code Generation Template

## Purpose

Context-rich code generation that matches your codebase. From Chapter 10.

## The Prompt

```
Language: [language and version]
Style: [coding conventions, e.g., "Follow PEP 8, use type hints"]
Dependencies: [what can/cannot be used]
Error handling: [your conventions]

Task: [what to implement]

Requirements:
- [requirement 1]
- [requirement 2]
- [requirement 3]

Context:
- This code will be used in: [where/how]
- Related existing code: [patterns to follow]
- Integration points: [what it connects to]

Output:
- The implementation
- Brief explanation of key decisions
- Any assumptions I should verify
```

## Usage Notes

- **More context = better output**: Include framework, existing patterns, constraints
- **Be specific about requirements**: Vague requirements produce vague code
- **Verify everything**: Compile, test, read the code yourself

## Variations

### Minimal (Quick Scripts)

```
Write a [language] function that [does what].

Requirements:
- [key constraint 1]
- [key constraint 2]

Keep it simple—this is a one-off script.
```

### Production-Grade

```
Language: [language] [version]
Framework: [framework] [version]
Style guide: [link or description]

Task: [detailed description]

Requirements:
- [functional requirement 1]
- [functional requirement 2]
- Handle errors: [specific error handling pattern]
- Logging: [logging conventions]
- Testing: [what tests to include]

Existing patterns to follow:
- See [file path] for similar implementation
- Use [existing utility/pattern] for [purpose]

Constraints:
- Must work with [existing system]
- Cannot use [prohibited dependency]
- Must handle [specific edge case]
```

### With Examples

```
Generate a function similar to this existing code:

```[language]
[paste example of similar function]
```

New function should:
- [what it does differently]
- Follow the same patterns for [error handling, naming, etc.]
```

## Refactoring Template

```
Refactoring goal: [what to improve]

Current code:
```[language]
[paste code]
```

Constraints:
- Keep the public API identical
- Do not change behavior for existing test cases
- [specific constraints]

Before showing code:
1. Explain your refactoring approach
2. Identify what will change
3. Note any edge cases that might behave differently

Then show the refactored code.
```

## Test Generation Template

```
Given this function:

```[language]
[paste function]
```

Generate test cases covering:

1. Normal operation (3-5 cases)
2. Edge cases:
   - Empty input
   - Single element
   - Very large input
   - Unicode/special characters
3. Error cases:
   - Invalid input types
   - Null/None values
   - Out-of-range values

For each test:
- Name that describes what it tests
- Clear assertion
- Comment explaining why this case matters
```

## Post-Generation Checklist

After receiving generated code:

- [ ] Does it compile/run?
- [ ] Did you read and understand it?
- [ ] Does it handle the edge cases you care about?
- [ ] Does it follow your codebase conventions?
- [ ] Are there any security issues?
- [ ] Did you write/run tests?
