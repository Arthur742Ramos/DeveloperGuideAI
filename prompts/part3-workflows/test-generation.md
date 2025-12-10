# Test Generation Template

## Purpose

Generate comprehensive test cases including edge cases you might not think of. From Chapter 10.

## The Prompt

```
Given this function:

```[language]
[paste function]
```

Generate test cases covering:

1. **Normal operation** (3-5 cases)
   - Typical inputs
   - Expected outputs

2. **Edge cases**
   - Empty input
   - Single element
   - Very large input
   - Boundary values
   - Unicode/special characters

3. **Error cases**
   - Invalid input types
   - Null/None values
   - Out-of-range values
   - Missing required fields

For each test:
- Descriptive name that explains what it tests
- Clear arrangement, action, assertion
- Comment explaining why this case matters
```

## Framework-Specific Templates

### Python (pytest)

```
Generate pytest tests for this function:

```python
[paste function]
```

Requirements:
- Use pytest fixtures where appropriate
- Use parametrize for similar test cases
- Include docstrings explaining each test
- Follow arrange-act-assert pattern
```

### JavaScript (Jest)

```
Generate Jest tests for this function:

```javascript
[paste function]
```

Requirements:
- Use describe blocks to group related tests
- Use beforeEach for common setup
- Include tests for async behavior if applicable
- Mock external dependencies
```

### Go

```
Generate Go tests for this function:

```go
[paste function]
```

Requirements:
- Use table-driven tests
- Include subtests with t.Run
- Test error cases explicitly
- Follow Go testing conventions
```

## Test Categories

### Unit Tests

```
Generate unit tests that:
- Test the function in isolation
- Mock all external dependencies
- Cover all code paths
- Test boundary conditions
```

### Integration Tests

```
Generate integration tests that:
- Test interaction with [dependency]
- Use real [database/service] in test mode
- Verify end-to-end behavior
- Clean up test data after
```

### Property-Based Tests

```
Generate property-based tests that verify:
- [invariant 1]: for all inputs, [property holds]
- [invariant 2]: [another property]

Use [hypothesis/fast-check/gopter] syntax.
```

## Adversarial Test Generation

```
You are a QA engineer trying to break this code:

```[language]
[paste code]
```

Generate adversarial test cases:
1. Inputs that might cause crashes
2. Inputs that might cause incorrect results
3. Inputs that might cause security issues
4. Inputs that might cause performance problems

For each: the input, why it's problematic, expected behavior.
```

## Test Review

```
Review these existing tests:

```[language]
[paste tests]
```

Check for:
1. Missing test cases (what's not covered?)
2. Weak assertions (what could pass incorrectly?)
3. Test isolation issues (do tests depend on each other?)
4. Flakiness risks (timing, randomness, external state)

Suggest specific improvements.
```

## Verification After Generation

- [ ] Do the tests actually run?
- [ ] Do they pass on correct implementation?
- [ ] Do they fail on incorrect implementation?
- [ ] Are assertions checking the right things?
- [ ] Are edge cases genuinely exercised?
