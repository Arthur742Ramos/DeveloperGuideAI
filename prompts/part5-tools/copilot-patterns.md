# GitHub Copilot Patterns

## Purpose

Effective patterns for IDE-integrated completion and chat. From Chapter 18.

## Inline Completion Patterns

### Comment-First Development

Write the comment, let Copilot complete:

```python
# Validate email address using regex
# Returns true if valid, false otherwise
# Should handle: plus addressing, subdomains, common TLDs
```

### Signature-First Development

Write descriptive signature, let Copilot implement:

```python
def calculate_shipping_cost(
    weight_kg: float,
    destination_country: str,
    shipping_method: str,  # "standard", "express", "overnight"
    is_fragile: bool = False
) -> float:
```

### Test-First Completion

Write tests, let Copilot suggest implementation:

```python
def test_parse_duration():
    assert parse_duration("2h30m") == 9000  # seconds
    assert parse_duration("45m") == 2700
    assert parse_duration("1h") == 3600

# Now write: def parse_duration(s: str) -> int:
```

## Copilot Chat Commands

### Explain Code

```
/explain

What does this regex do? What inputs would match?
```

### Generate Tests

```
/tests

Generate unit tests covering:
- Normal operation
- Edge cases (empty, large, special characters)
- Error cases (invalid input, null)
```

### Fix Errors

```
/fix

The error is: TypeError: cannot unpack non-iterable NoneType
This happens when API returns no results. Handle gracefully.
```

### Generate Documentation

```
/doc

Generate docstring with:
- Brief description
- Parameters with types
- Return value
- Example usage
```

## Agent Mode (@workspace)

For cross-file operations:

```
@workspace Add a new /api/health endpoint that returns:
- Server uptime
- Database connection status
- Cache hit rate

Follow existing patterns in /api/status
```

## Multi-File Operations

```
Rename the User class to Account across the codebase:
- Class definition
- All imports
- Database migrations
- API serializers
- Test files
```

**Warning**: Always verify multi-file changes with `git diff` and search for the old name.

## Repository Instructions

Create `.github/copilot-instructions.md`:

```markdown
# Project: [Name]

## Tech Stack
- [Language] [version]
- [Framework] [version]
- [Database]

## Commands
- `npm run build` - Compile
- `npm test` - Run tests
- `npm run lint` - Check style

## Conventions
- [Convention 1]
- [Convention 2]
- [Convention 3]

## Patterns
- Database queries go in src/repositories/
- Business logic goes in src/services/
- See src/services/userService.ts for standard pattern
```

## Scoped Instructions

For different parts of the codebase, create `.github/instructions/*.instructions.md`:

```markdown
---
applyTo: "src/api/**"
---
# API Route Guidelines
- All routes require authentication middleware
- Use validateRequest() for input validation
- Return appropriate HTTP status codes
```

## When Copilot Works Best

- Quick completions within a file
- Following established patterns
- Boilerplate code
- Explaining unfamiliar code

## When to Use Something Else

- Multi-step investigations (use terminal agent)
- Complex refactoring (use terminal agent)
- Codebase-wide changes (use terminal agent with verification)
