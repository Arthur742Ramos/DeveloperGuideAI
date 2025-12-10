# GitHub Copilot Complete Guide

Everything you need to use GitHub Copilot effectively, in one document.

---

## Overview

GitHub Copilot is an IDE-integrated AI assistant. It works in two modes:
- **Inline completion**: Suggests code as you type
- **Chat**: Conversational interface for explanations, generation, and refactoring

Best for: Quick completions, explaining code, small edits within a file.
Use something else for: Multi-file refactoring, complex debugging, codebase-wide changes.

---

## Inline Completion Patterns

### Comment-First Development

Write the comment, let Copilot complete the implementation:

```python
# Validate email address using regex
# Returns true if valid, false otherwise
# Handle: plus addressing, subdomains, common TLDs
def validate_email(email: str) -> bool:
    # Copilot completes here
```

### Signature-First Development

Write a descriptive function signature with typed parameters:

```python
def calculate_shipping_cost(
    weight_kg: float,
    destination_country: str,
    shipping_method: str,  # "standard", "express", "overnight"
    is_fragile: bool = False
) -> float:
    # Copilot completes here
```

### Test-First Completion

Write tests first, then let Copilot suggest implementation:

```python
def test_parse_duration():
    assert parse_duration("2h30m") == 9000  # seconds
    assert parse_duration("45m") == 2700
    assert parse_duration("1h") == 3600

# Now type: def parse_duration(s: str) -> int:
# Copilot will suggest an implementation that passes the tests
```

### Prompt with Examples

Provide an example in a comment to guide the pattern:

```python
# Convert snake_case to camelCase
# Example: "user_first_name" -> "userFirstName"
def snake_to_camel(s: str) -> str:
```

---

## Chat Commands

### /explain - Understand Code

```
/explain

What does this regex do? What inputs would match and not match?
```

```
/explain

Walk through this function step by step. What are the edge cases?
```

### /tests - Generate Tests

```
/tests

Generate unit tests covering:
- Normal operation with typical inputs
- Edge cases (empty, single element, large input)
- Error cases (invalid input, null)
```

### /fix - Fix Errors

```
/fix

The error is: TypeError: cannot unpack non-iterable NoneType
This happens when the API returns no results. Handle gracefully.
```

### /doc - Generate Documentation

```
/doc

Generate docstring with:
- Brief description
- Parameters with types
- Return value
- Example usage
```

### /simplify - Reduce Complexity

```
/simplify

This function is too complex. Break it down or simplify the logic.
```

---

## Agent Mode (@workspace)

For operations that span multiple files:

```
@workspace Add a new /api/health endpoint that returns:
- Server uptime
- Database connection status
- Cache hit rate

Follow existing patterns in /api/status
```

```
@workspace Find all usages of the deprecated `oldFunction` and show me where they are.
```

```
@workspace What files would I need to modify to add user roles to our auth system?
```

---

## Multi-File Operations

Ask Copilot to help with renames or refactors:

```
Rename the User class to Account across the codebase:
- Class definition
- All imports
- Database migrations
- API serializers
- Test files
```

**Warning**: Always verify multi-file changes:
```bash
git diff
git grep "User"  # Check for missed occurrences
```

---

## Repository Instructions

Create `.github/copilot-instructions.md` in your repo:

```markdown
# Project: MyApp

## Tech Stack
- Python 3.11
- FastAPI 0.100
- PostgreSQL 15
- Redis for caching

## Commands
- `make dev` - Start development server
- `make test` - Run pytest
- `make lint` - Run ruff

## Code Style
- Follow PEP 8
- Use type hints everywhere
- Docstrings for public functions

## Patterns
- Database queries: Use repositories in src/repositories/
- Business logic: Goes in src/services/
- Example service: See src/services/user_service.py

## Conventions
- snake_case for functions and variables
- PascalCase for classes
- ALL_CAPS for constants

## Do Not
- Use print() for logging (use structlog)
- Write raw SQL outside repositories
- Commit .env files
```

---

## Scoped Instructions

For different parts of your codebase, create `.github/instructions/*.instructions.md`:

**API routes** (`.github/instructions/api.instructions.md`):
```markdown
---
applyTo: "src/api/**"
---
# API Route Guidelines

- All routes require authentication middleware
- Use validateRequest() for input validation
- Return appropriate HTTP status codes
- Log all errors with request context
```

**Frontend** (`.github/instructions/frontend.instructions.md`):
```markdown
---
applyTo: "src/frontend/**"
---
# Frontend Guidelines

- Use functional components with hooks
- CSS modules for styling (no inline styles)
- All text must use i18n translation keys
```

---

## Effective Prompts for Chat

### Code Review
```
Review this code for production readiness:
- Error handling
- Edge cases
- Performance
- Security

Be direct about issues.
```

### Explain Complex Code
```
Explain this code as if I need to modify it:
- What's the main purpose?
- What are the key steps?
- What assumptions does it make?
- What would break if I changed X?
```

### Generate with Context
```
Generate a function to [task].

Requirements:
- [requirement 1]
- [requirement 2]

Follow the same patterns as [existing similar code].
```

### Debug Help
```
This code throws [error] when [condition].

```python
[paste code]
```

What's causing this and how do I fix it?
```

---

## Keyboard Shortcuts (VS Code)

| Action | Shortcut |
|--------|----------|
| Accept suggestion | Tab |
| Reject suggestion | Esc |
| Next suggestion | Alt+] |
| Previous suggestion | Alt+[ |
| Open Copilot Chat | Ctrl+I |
| Inline chat | Ctrl+Shift+I |

---

## When Copilot Works Best

- Quick completions within a single file
- Following established patterns in your codebase
- Boilerplate code (getters, setters, simple CRUD)
- Explaining unfamiliar code
- Generating docstrings and comments
- Simple refactoring within a file

## When to Use Something Else

- Multi-step debugging requiring file access (use Claude Code or Codex)
- Complex refactoring across many files (use terminal agent)
- Codebase-wide changes requiring verification (use terminal agent)
- Tasks requiring shell commands (use terminal agent)

---

## Common Pitfalls

### Accepting Without Reading
Copilot suggestions look plausible but may have bugs. Always read before accepting.

### Over-Reliance on Completions
Sometimes typing directly is faster than waiting for and evaluating suggestions.

### Ignoring Context Windows
Long files may exceed context. Copilot might miss important code above/below.

### Not Providing Enough Context
Vague prompts produce vague code. Be specific about requirements.

---

## Verification Checklist

After accepting Copilot suggestions:

- [ ] Read the generated code
- [ ] Check that it does what you asked
- [ ] Verify edge case handling
- [ ] Run existing tests
- [ ] Write new tests if needed
- [ ] Check for security issues
