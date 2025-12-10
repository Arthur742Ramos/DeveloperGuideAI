# Agent Instruction File Templates

Templates for configuring AI coding agents. Copy to your project and customize.

## Quick Setup

```bash
# For Claude Code
cp CLAUDE.md.template /path/to/your/project/CLAUDE.md

# For OpenAI Codex CLI
cp AGENTS.md.template /path/to/your/project/AGENTS.md

# For GitHub Copilot
mkdir -p /path/to/your/project/.github
cp copilot-instructions.md.template /path/to/your/project/.github/copilot-instructions.md
```

## Files

| Template | Tool | Location in Project |
|----------|------|---------------------|
| `CLAUDE.md.template` | Claude Code | `CLAUDE.md` (root) |
| `AGENTS.md.template` | OpenAI Codex CLI | `AGENTS.md` (root) |
| `copilot-instructions.md.template` | GitHub Copilot | `.github/copilot-instructions.md` |

## Customization Guide

### 1. Replace Placeholders

Templates use `[BRACKETS]` for values you must provide:

```markdown
# Project: [PROJECT_NAME]

## Commands
- `[BUILD_COMMAND]` - Build the project
- `[TEST_COMMAND]` - Run tests
```

### 2. Add Your Conventions

Include project-specific rules:

```markdown
## Conventions
- Use [your style guide]
- Database queries go in [your pattern]
- Error responses use [your format]
```

### 3. Include Key Paths

Help the AI find important code:

```markdown
## Key Files
- Authentication: src/auth/middleware.ts
- Database models: src/models/
- API routes: src/routes/
```

### 4. List Constraints

Prevent common mistakes:

```markdown
## Do Not
- Modify files in /generated (auto-generated)
- Change database schema without migration
- Commit .env files
```

## Best Practices

### Be Concise

AI can reliably follow ~150-200 instructions. Keep it terse:

```markdown
# Good
- Use TypeScript strict mode
- Tests required for API changes

# Too verbose
- When writing TypeScript code, please ensure that you have enabled
  strict mode in the tsconfig.json file to catch potential type errors...
```

### Use Pointers, Not Content

Reference files instead of embedding content:

```markdown
# Good
- See src/services/userService.ts:15 for service pattern

# Bad
- Services should look like this: [50 lines of code]
```

### Iterate Based on Mistakes

When AI repeatedly makes the same error, add a specific instruction:

```markdown
## Learned Constraints
- Always run typecheck before committing (added after CI failures)
- Use snake_case for database columns (added after migration issues)
```

## Tool-Specific Notes

### Claude Code

- Reads `CLAUDE.md` from repo root
- Supports `CLAUDE.local.md` for personal settings (add to .gitignore)
- Nested `CLAUDE.md` files add context for subdirectories
- Run `/init` to generate starter file

### OpenAI Codex CLI

- Reads `AGENTS.md` from repo root
- Supports `AGENTS.override.md` for personal customization
- Also reads from `~/.codex/AGENTS.md` globally
- Run `codex /init` to generate starter file

### GitHub Copilot

- Reads `.github/copilot-instructions.md`
- Supports scoped instructions in `.github/instructions/*.instructions.md`
- Also reads `AGENTS.md` and `CLAUDE.md` if present
- Personal settings in VS Code settings
