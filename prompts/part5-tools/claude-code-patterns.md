# Claude Code Patterns

## Purpose

Effective patterns for terminal-based agentic coding. From Chapter 19.

## Basic Patterns

### Context-Rich Requests

```
Look at src/api/users.py and add a new endpoint for user deletion.
Follow the same patterns as the existing create and update endpoints.
Make sure to add appropriate tests in tests/test_users.py.
```

### Multi-Step Tasks

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

```
Running pytest gives this error:

FAILED tests/test_api.py::test_create_order - AssertionError:
Expected status 201 but got 400

Investigate why and fix it.
```

### Large Codebase Navigation

```
The authentication logic is in src/auth/.
The middleware is in src/middleware/auth.py.
Database models are in src/models/.

I need to add role-based access control.
Start by understanding the current auth flow, then propose an approach.
```

## Git Integration

### Commit Changes

```
Create a commit for the changes we just made.
Use a descriptive commit message following conventional commits format.
```

### Create Pull Request

```
Create a pull request for this feature branch.
Summarize the changes and note any areas reviewers should pay attention to.
```

## CLAUDE.md Configuration

Create `CLAUDE.md` in your project root:

```markdown
# Project: [Name]

## Structure
- src/routes/ - Express route handlers
- src/services/ - Business logic
- src/repositories/ - Database access
- src/models/ - TypeScript interfaces

## Commands
- `npm run dev` - Start development server
- `npm test` - Run Jest tests
- `npm run typecheck` - Check TypeScript

## Conventions
- Always run typecheck after code changes
- Use repository pattern for all database access
- Prefer single test runs: npm test -- path/to/test
- Error responses use {success: false, error: string}

## Constraints
- Never modify migration files directly
- Do not commit .env files
- Keep route handlers thin - logic goes in services
```

## File Locations

- **Repository root**: `CLAUDE.md` (most common)
- **Subdirectories**: Additional `CLAUDE.md` for context-specific guidance
- **Global**: `~/.claude/CLAUDE.md` for all sessions
- **Local override**: `CLAUDE.local.md` (add to .gitignore)

## Writing Tips

- **Be terse**: Short declarative statements, not paragraphs
- **Use file references**: "See src/services/userService.ts:15 for pattern"
- **Iterate on mistakes**: Add instructions when Claude repeatedly errs
- **Separate concerns**: Use `.local.md` for personal preferences

## Safety Patterns

### Review Changes

```
Before committing, show me what changed with git diff.
```

### Explicit Approval

```
Before executing any command that modifies files:
1. Show me the exact command
2. Explain what it will do
3. Wait for my explicit "proceed"
```

### Scope Limits

```
For this task, only modify files in src/api/.
Do not touch tests until I ask.
```

## When Claude Code Works Best

- Complex refactoring across files
- Debugging with file access
- Multi-file feature implementation
- Git operations

## When to Use Something Else

- Quick single-line completions (use IDE)
- Explaining code in current file (use IDE chat)
