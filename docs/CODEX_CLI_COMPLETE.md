# OpenAI Codex CLI Complete Guide

Everything you need to use Codex CLI effectively, in one document.

---

## Overview

Codex CLI is a terminal-based coding assistant from OpenAI. Key features:
- Three approval modes for different safety levels
- Can read/write files and run commands
- Supports cloud tasks for async work
- Uses AGENTS.md for project configuration

Best for: Well-defined tasks, routine maintenance, batch operations with approval.
Use something else for: Quick completions (use IDE), complex investigation requiring judgment.

---

## Approval Modes

| Mode | File Changes | Commands | Best For |
|------|--------------|----------|----------|
| Suggest | Ask first | Ask first | Unfamiliar codebases, learning |
| Auto-Edit | Automatic | Ask first | Regular development |
| Full Auto | Automatic | Automatic | Sandboxed, well-tested environments |

### Choosing a Mode

| Situation | Recommended Mode |
|-----------|------------------|
| Unfamiliar codebase | Suggest |
| Production code | Suggest or Auto-Edit |
| Personal project | Auto-Edit |
| Well-tested with rollback | Full Auto (with caution) |
| Learning/exploring | Suggest |
| Routine tasks | Auto-Edit |

### Safety with Full Auto

If using Full Auto:
- Only in sandboxed environments
- Only on projects with good test coverage
- Never on production code directly
- Have rollback ready (clean git state)

---

## Basic Patterns

### Direct Tasks

Clear, specific requests work best:

```
Add input validation to the signup form. Validate:
- Email format
- Password strength (8+ chars, mixed case, number)
- Username (alphanumeric, 3-20 chars)

Show validation errors inline below each field.
```

### Investigation Requests

Ask Codex to find and fix:

```
The build is failing with "Module not found: react-query".
Investigate why and fix it. Check package.json, import statements,
and any recent changes.
```

### Architectural Questions

Get recommendations before implementing:

```
I need to add real-time updates to our dashboard.
What approaches would work with our stack (React, Express, PostgreSQL)?
Consider: WebSockets, Server-Sent Events, polling.
Recommend one and explain why.
```

### Migration Tasks

Codex handles repetitive migrations well:

```
Migrate all unit tests from Jest to Vitest.

Constraints:
- Keep test logic identical
- Update imports
- Convert Jest-specific APIs

Start with tests/ directory, one file at a time.
```

---

## AGENTS.md Configuration

Create `AGENTS.md` in your project root:

### Basic Template

```markdown
# Project: MyApp

## Quick Start
```bash
npm install
npm run dev      # Start dev server
npm test         # Run tests
npm run build    # Production build
```

## Architecture
- React 18 frontend in /src/app
- Node.js API in /src/api
- Shared types in /src/types
- Database models in /src/models

## Standards
- TypeScript strict mode everywhere
- Tests required for API endpoints
- Use React Query for server state
- CSS modules for styling

## Key Files
- src/api/routes.ts - API route definitions
- src/app/App.tsx - Main React component
- src/types/index.ts - Shared type definitions

## Do Not
- Modify files in /src/generated (auto-generated)
- Change database schema without migration
- Push directly to main
- Skip TypeScript checks
```

### File Discovery Order

Codex searches for instruction files in this order:
1. Global: `~/.codex/AGENTS.md`
2. Repository root: `AGENTS.md`
3. Nested directories: Additional `AGENTS.md` files add context
4. Fallback names: `TEAM_GUIDE.md`, `.agents.md`

### Directory-Scoped Instructions (Monorepos)

```
project/
  AGENTS.md              # Global rules
  packages/
    api/
      AGENTS.md          # API-specific rules
    frontend/
      AGENTS.md          # Frontend-specific rules
```

---

## Cloud Tasks

Run tasks asynchronously in the cloud:

```bash
codex cloud "Generate comprehensive tests for the user service.
Target 80% coverage. Create a PR when done."
```

Good for:
- Long-running tasks
- Tasks you want to review later
- Batch operations

---

## Common Commands

```bash
# Generate starter AGENTS.md
codex /init

# Check if instructions loaded
codex status

# Debug MCP issues
codex --mcp-debug

# Run with specific approval mode
codex --suggest "task description"
codex --auto-edit "task description"
codex --full-auto "task description"
```

---

## Effective Prompts

### Feature Implementation

```
Add a user profile page at /profile that shows:
- User avatar (from Gravatar)
- Name and email
- Account creation date
- Edit button that opens a modal

Use existing patterns from src/pages/Settings.tsx.
```

### Bug Fixes

```
Bug: Users report slow page loads on the dashboard.

Steps to reproduce:
1. Log in with a user who has many items
2. Navigate to dashboard
3. Observe 5+ second load time

Find the performance issue and fix it.
```

### Code Cleanup

```
Clean up src/utils/helpers.ts:
- Remove unused functions
- Add TypeScript types
- Split into logical modules
- Update all import statements

Show plan before making changes.
```

### Test Generation

```
Generate tests for src/services/orderService.ts.

Requirements:
- Use Vitest
- Mock database calls
- Cover happy path and error cases
- Aim for 80% coverage

Follow patterns in tests/services/userService.test.ts.
```

---

## Working with Approval

### Suggest Mode

Every action requires approval. Use when:
- Learning a new codebase
- Sensitive code
- You want to understand what's happening

### Auto-Edit Mode

Files are edited automatically, commands still ask. Use when:
- Regular development
- You trust file changes but want command visibility
- Iterating quickly

### Reviewing Suggestions

When Codex suggests changes:
1. Read the proposed change
2. Check if it makes sense
3. Consider side effects
4. Approve or request modifications

---

## Debugging with Codex

### Provide Full Context

```
Test failure:

```
FAIL tests/api.test.ts
  ✕ should create user (45 ms)
    Expected: 201
    Received: 400

    Body: { error: "email is required" }
```

The test is in tests/api.test.ts and the endpoint is in src/api/users.ts.
Find and fix the issue.
```

### Step-by-Step Investigation

```
Help me debug this systematically:

1. First, show me the test code
2. Then show me the endpoint
3. Identify the mismatch
4. Propose a fix
```

---

## Comparison: Codex CLI vs Claude Code

| Aspect | Codex CLI | Claude Code |
|--------|-----------|-------------|
| Approval modes | Three levels | Single mode with prompts |
| Cloud tasks | Yes | No |
| Instruction file | AGENTS.md | CLAUDE.md |
| Autonomy control | Granular | Conversation-based |
| Best for | Defined tasks, batch work | Exploration, debugging |

---

## Best Practices

### Start with Suggest Mode

Until you understand how Codex behaves on your codebase, use Suggest mode.

### Write Good AGENTS.md

Invest time in your instruction file. Clear guidance produces better results.

### Scope Tasks Clearly

```
# Good - specific scope
Add email validation to the signup form

# Less good - vague scope
Improve the signup form
```

### Verify Results

Even in Auto-Edit mode, verify:
- Tests pass
- No unintended changes
- Code does what you asked

### Use Cloud for Long Tasks

If a task will take more than a few minutes, use cloud mode.

---

## Troubleshooting

### Codex Doesn't See My Instructions

```bash
codex status  # Check if AGENTS.md loaded
```

Ensure AGENTS.md is in project root or check for typos.

### Unexpected File Changes

Review with:
```bash
git diff
git status
```

Revert if needed:
```bash
git checkout -- .
```

### MCP Issues

```bash
codex --mcp-debug
```

Check server logs and configuration.

---

## Verification Checklist

After Codex makes changes:

- [ ] Review all changed files: `git diff`
- [ ] Run tests: Do they pass?
- [ ] Run linter: Any new issues?
- [ ] Manual test: Does it work?
- [ ] Check nothing unexpected changed
- [ ] Commit with clear message
