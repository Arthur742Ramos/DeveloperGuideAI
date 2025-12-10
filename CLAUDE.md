# DeveloperGuideAI

Practical resources for AI-assisted software development.

## Purpose

This repository provides:
- Prompt templates developers can copy and adapt
- Working code examples for practice
- Reference implementations of effective patterns

Everything here should be **immediately usable** by developers working with AI coding tools.

## Structure

```
prompts/          # Prompt templates organized by topic
  part1-mindset/  # Foundations and mental models
  part2-patterns/ # Core prompting patterns
  part3-workflows/# Practical development workflows
  part4-beyond/   # Safety and evaluation
  part5-tools/    # Tool-specific guidance

scripts/          # CLI wrappers that use the prompts
examples/         # Code for exercises (buggy code, review targets, data)
instruction-files/# Templates for CLAUDE.md, AGENTS.md, etc.
mcp/              # MCP server implementations
resources/        # Curated external links
```

## Conventions

### Prompt Templates

All templates use `[BRACKETED_PLACEHOLDERS]` for values users must provide:
```markdown
Role: You are a [LANGUAGE] expert reviewing code for [FOCUS_AREA].
```

Common placeholders:
- `[LANGUAGE]` - Programming language
- `[FILE_CONTENT]` - Code to analyze
- `[CONTEXT]` - Project-specific background
- `[CONSTRAINTS]` - Specific requirements or limitations

### File Naming
- Prompts: `kebab-case.md` (e.g., `code-review.md`)
- Scripts: `kebab-case.sh` or `snake_case.py`
- Examples: Descriptive names matching their bug/purpose

### Markdown Style
- Use ATX headers (`#`, `##`, not underlines)
- Code blocks specify language: ` ```python `
- One sentence per line in prose (easier diffs)
- No trailing whitespace

### Code Examples
- **Buggy code**: Must have corresponding `.solution.md`
- **Solutions**: Explain the bug, show the fix, teach the lesson
- **All code**: Must be syntactically valid and runnable

## Key Files

| Path | Purpose |
|------|---------|
| `prompts/README.md` | Index of all templates with usage guide |
| `scripts/prompt-runner.py` | Generic template executor |
| `examples/README.md` | Exercise index with difficulty ratings |
| `instruction-files/README.md` | Guide to agent instruction files |

## Do Not

- Add real API keys, tokens, or credentials (even "fake" ones that look real)
- Include overly verbose explanations (keep templates concise)
- Create prompts without clear placeholders
- Add examples without solutions
- Use external dependencies in scripts without documenting them

## Common Tasks

### Adding a new prompt template

1. Identify the topic area it supports
2. Create file in appropriate `prompts/partN-*/` directory
3. Include header comment with:
   - When to use this prompt
   - Required placeholders
   - Expected output format
4. Add entry to `prompts/README.md` index

Pattern to follow: `prompts/part2-patterns/code-review.md`

### Adding a buggy code example

1. Create the buggy file in `examples/buggy-code/`
2. Include header comment explaining:
   - What the bug type is
   - Expected vs actual behavior
   - Difficulty level (Easy/Medium/Hard)
3. Create matching `.solution.md` with:
   - Bug explanation
   - Fixed code
   - Lessons learned
4. Update `examples/README.md` index

Pattern to follow: `examples/buggy-code/off_by_one.py`

### Adding a script wrapper

1. Create in `scripts/` directory
2. Include:
   - Shebang line (`#!/bin/bash` or `#!/usr/bin/env python3`)
   - Usage comment at top
   - `AI_CLI` environment variable support
   - Input validation with helpful error messages
3. Update `scripts/README.md`

Pattern to follow: `scripts/review.sh`

## Quality Checks

Before committing, verify:

```bash
# All Python files are valid syntax
python -m py_compile scripts/*.py examples/**/*.py

# All shell scripts pass shellcheck (if installed)
shellcheck scripts/*.sh

# No secrets detected
git diff --cached | grep -iE "(sk_live|api_key|password|secret)" && echo "SECRETS FOUND"
```

## Repository Structure

| Part | Focus | Location |
|------|-------|----------|
| Part 1 | Mindset & Foundations | `prompts/part1-mindset/` |
| Part 2 | Prompting Patterns | `prompts/part2-patterns/` |
| Part 3 | Practical Workflows | `prompts/part3-workflows/` |
| Part 4 | Safety & Evaluation | `prompts/part4-beyond/` |
| Part 5 | Tool-Specific | `prompts/part5-tools/`, `mcp/`, `instruction-files/` |

## Design Principles

1. **Prompts are contracts**: Every template clearly specifies role, task, constraints
2. **Verify outputs**: Examples include test cases that reveal bugs
3. **Iterate through conversation**: Templates support multi-turn refinement
4. **Separate concerns**: Each file does one thing well
5. **Keep humans in the loop**: Scripts print prompts by default, require explicit AI_CLI

## Contribution Notes

This repo welcomes contributions that:
- Fix bugs in examples (typos, syntax errors)
- Add new prompt templates for uncovered use cases
- Improve solutions with clearer explanations
- Add translations of prompts (in `prompts/translations/`)

Open an issue first for:
- New example categories
- Structural changes
- Removing existing content
