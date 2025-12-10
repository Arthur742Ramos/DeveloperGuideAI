# Claude Code Complete Guide

Everything you need to use Claude Code effectively, in one document.

---

## Overview

Claude Code is a terminal-based agentic coding assistant. It can:
- Read and write files
- Execute shell commands
- Search codebases
- Create commits and PRs

Best for: Complex refactoring, debugging with file access, multi-file features, git operations.
Use something else for: Quick single-line completions (use IDE), inline code explanations (use IDE chat).

---

## Basic Patterns

### Context-Rich Requests

Tell Claude Code what files to look at and what patterns to follow:

```
Look at src/api/users.py and add a new endpoint for user deletion.
Follow the same patterns as the existing create and update endpoints.
Make sure to add appropriate tests in tests/test_users.py.
```

### Multi-Step Tasks

Break down what you need into clear steps:

```
I need to add Redis caching to our API:
1. Add redis to requirements.txt
2. Create a cache utility module in src/utils/cache.py
3. Add caching to the get_user endpoint
4. Add cache invalidation to update_user and delete_user
5. Add tests for the caching behavior
6. Run the tests to make sure everything works
```

### Debugging with Context

Provide the error and let Claude Code investigate:

```
Running pytest gives this error:

FAILED tests/test_api.py::test_create_order - AssertionError:
Expected status 201 but got 400

Investigate why and fix it.
```

### Large Codebase Navigation

Point to relevant areas before asking for changes:

```
The authentication logic is in src/auth/.
The middleware is in src/middleware/auth.py.
Database models are in src/models/.

I need to add role-based access control.
Start by understanding the current auth flow, then propose an approach.
```

---

## Git Integration

### Review Changes Before Committing

```
Show me what changed with git diff before we commit.
```

### Create Commits

```
Create a commit for the changes we just made.
Use a descriptive commit message following conventional commits format.
```

### Create Pull Requests

```
Create a pull request for this feature branch.
Summarize the changes and note any areas reviewers should pay attention to.
```

### Check Status

```
What's the current git status? Any uncommitted changes?
```

---

## CLAUDE.md Configuration

Create `CLAUDE.md` in your project root. This is the most important file for getting good results.

### Basic Template

```markdown
# Project: MyApp

## Commands
- `npm run dev` - Start development server
- `npm test` - Run Jest tests
- `npm run typecheck` - Check TypeScript
- `npm run lint` - Run ESLint

## Structure
- src/routes/ - Express route handlers
- src/services/ - Business logic
- src/repositories/ - Database access
- src/models/ - TypeScript interfaces
- tests/ - Jest tests mirror src/ structure

## Conventions
- Use repository pattern for all database access
- Error responses: {success: false, error: string}
- Keep route handlers thin - logic goes in services
- Prefer single test runs: npm test -- path/to/test

## Key Files
- src/services/userService.ts - Standard service pattern
- src/repositories/baseRepository.ts - Repository base class
- src/middleware/auth.ts - Authentication middleware

## Do Not
- Modify migration files directly
- Commit .env files
- Use console.log (use logger from src/utils/logger)
- Skip TypeScript checks
```

### File Locations

| Location | Purpose |
|----------|---------|
| `CLAUDE.md` (repo root) | Main instructions, loaded automatically |
| `subdirectory/CLAUDE.md` | Context-specific, adds to root |
| `~/.claude/CLAUDE.md` | Global, applies to all sessions |
| `CLAUDE.local.md` | Personal overrides (gitignore this) |

### Writing Tips

**Be terse**: Short declarative statements, not paragraphs.
```markdown
# Good
- Run typecheck after code changes
- Use repository pattern for DB access

# Too verbose
- When making changes to the codebase, please ensure you run the
  TypeScript compiler to check for type errors before committing...
```

**Use file references**: Point to examples instead of describing patterns.
```markdown
# Good
- Service pattern: See src/services/userService.ts:15

# Less useful
- Services should have a constructor that takes repositories...
```

**Iterate on mistakes**: When Claude repeatedly makes the same error, add a specific instruction.
```markdown
## Learned Constraints
- Always run typecheck (added after CI failures)
- Use snake_case for DB columns (added after migration issues)
```

---

## Safety Patterns

### Review Before Committing

Always check changes before they're committed:

```
Before committing, show me what changed with git diff.
```

### Explicit Approval for Dangerous Operations

```
Before executing any command that modifies files:
1. Show me the exact command
2. Explain what it will do
3. Wait for my explicit "proceed"
```

### Scope Limits

Constrain what Claude Code can touch:

```
For this task, only modify files in src/api/.
Do not touch tests until I ask.
```

```
Only modify the function `processOrder`. Don't change anything else in this file.
```

### Staged Rollout

For risky changes:

```
Let's do this in stages:
1. First, show me the plan
2. Then make changes to one file
3. Let me verify it works
4. Then proceed to other files
```

---

## Effective Prompts

### Feature Implementation

```
Add a password reset feature:

Requirements:
- User requests reset via email
- Token expires after 1 hour
- Invalidate token after use

Existing patterns:
- Email sending: src/services/emailService.ts
- Token generation: src/utils/crypto.ts

Start by proposing the approach, then implement.
```

### Bug Investigation

```
Users report that sometimes orders are duplicated.

It seems to happen when they click the submit button multiple times.

Investigate:
1. How does the order creation endpoint handle duplicate requests?
2. Is there any idempotency mechanism?
3. Propose a fix
```

### Refactoring

```
The function `processPayment` in src/services/paymentService.ts is 200 lines.

Refactor it:
- Extract helper functions
- Improve error handling
- Keep the same public interface
- Add comments explaining the flow

Show me the plan before making changes.
```

### Code Review

```
Review the changes in this PR:

git diff main...HEAD

Check for:
- Logic errors
- Missing error handling
- Security issues
- Performance concerns

Be specific about what to fix.
```

---

## Debugging Sessions

### Start with Context

```
The test `test_user_creation` passes locally but fails in CI with a timeout.

Relevant files:
- tests/test_users.py
- src/services/userService.py
- .github/workflows/test.yml

Investigate why.
```

### Follow the Trail

```
Based on what you found, check [next thing].
```

```
That's interesting. What does [related file] show?
```

### Confirm Understanding

```
Before you suggest a fix, explain what you think is causing this.
```

---

## Working with Large Codebases

### Orientation

```
I'm new to this codebase. Give me an overview:
- What's the main entry point?
- How is it structured?
- What are the key patterns used?
```

### Finding Things

```
Where is [functionality] implemented? Search for it.
```

```
Show me all the places that call [function name].
```

### Understanding Flow

```
Trace the request flow from [endpoint] through to the database.
What files are involved?
```

---

## Common Tasks

### Add a New Endpoint

```
Add a GET /api/users/:id/orders endpoint that returns a user's order history.

Follow patterns from:
- src/routes/users.ts for routing
- src/services/orderService.ts for service layer
- tests/routes/users.test.ts for testing
```

### Add Tests

```
Add tests for src/services/orderService.ts.

Cover:
- Normal operation
- Edge cases (no orders, invalid user)
- Error handling

Follow patterns in tests/services/userService.test.ts.
```

### Fix a Bug

```
Bug: The /api/search endpoint returns 500 when the query is empty.

Find the bug and fix it. Add a test case that would have caught this.
```

### Update Dependencies

```
Update the axios dependency to the latest version.

1. Update package.json
2. Check if there are breaking changes
3. Run tests
4. Fix any issues
```

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Accept current proposal | Enter |
| Reject proposal | Esc |
| Interrupt generation | Ctrl+C |

---

## Verification Checklist

After Claude Code makes changes:

- [ ] Review the diff: `git diff`
- [ ] Run tests: Does everything pass?
- [ ] Run linting: Any new issues?
- [ ] Manual test: Does it work as expected?
- [ ] Check edge cases: Did you test unusual inputs?
- [ ] Security review: Any new vulnerabilities?
