# OpenAI Codex CLI Patterns

## Purpose

Effective patterns for Codex CLI with its approval modes. From Chapter 20.

## Approval Modes

| Mode | Behavior | Best For |
|------|----------|----------|
| Suggest | You approve each action | Unfamiliar codebases, learning |
| Auto-Edit | Files auto, commands ask | Regular development |
| Full Auto | Full autonomy | Well-tested, sandboxed environments |

## Basic Patterns

### Direct Tasks

```
Add input validation to the signup form. Validate:
- Email format
- Password strength (8+ chars, mixed case, number)
- Username (alphanumeric, 3-20 chars)

Show validation errors inline below each field.
```

### Investigation Requests

```
The build is failing with "Module not found: react-query".
Investigate why and fix it. Check package.json, import statements,
and any recent changes.
```

### Architectural Questions

```
I need to add real-time updates to our dashboard.
What approaches would work with our stack (React, Express, PostgreSQL)?
Consider: WebSockets, Server-Sent Events, polling.
Recommend one and explain why.
```

## AGENTS.md Configuration

Create `AGENTS.md` in your project root:

```markdown
# Project: [Name]

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
- Use existing hooks in /src/hooks for data fetching

## Standards
- TypeScript strict mode everywhere
- Tests required for API endpoints
- Use React Query for server state
- CSS modules for styling (no inline styles)

## Do Not
- Modify files in /src/generated (auto-generated)
- Change database schema without migration
- Push directly to main
```

## File Discovery

Codex searches for instruction files in order:
1. Global: `~/.codex/AGENTS.md`
2. Repository root: `AGENTS.md`
3. Directory chain: Additional `AGENTS.md` files in nested directories
4. Fallback names: `TEAM_GUIDE.md`, `.agents.md`

## Directory-Scoped Instructions

For monorepos:

```
project/
  AGENTS.md              # Global rules
  packages/
    api/
      AGENTS.md          # API-specific rules
    frontend/
      AGENTS.md          # Frontend-specific rules
```

## Cloud Tasks

Run tasks asynchronously:

```bash
codex cloud "Generate comprehensive tests for the user service.
Target 80% coverage. Create a PR when done."
```

## Choosing Approval Mode

| Situation | Mode |
|-----------|------|
| Unfamiliar codebase | Suggest |
| Production code | Suggest or Auto-Edit |
| Personal project | Auto-Edit |
| Well-tested codebase | Full Auto (with caution) |
| Learning/exploring | Suggest |
| Routine tasks | Auto-Edit |

## Safety with Full Auto

If using Full Auto:
- Only in sandboxed environments
- Only on projects with good test coverage
- Never on production code
- Have rollback ready

## Useful Commands

```bash
# Generate starter AGENTS.md
codex /init

# Check if instructions loaded
codex status

# Debug MCP issues
codex --mcp-debug
```
