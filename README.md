# The Developer's Guide to AI - Companion Repository

Companion resources for [The Developer's Guide to AI: Patterns, Tools, and Workflows](https://github.com/Arthur742Ramos/AIBook).

## What's Here

```
DeveloperGuideAI/
├── prompts/              # Ready-to-use prompt templates by chapter
├── scripts/              # CLI wrappers for common AI tasks
├── instruction-files/    # CLAUDE.md, AGENTS.md, copilot-instructions templates
├── mcp/                  # MCP server examples (Python, TypeScript)
├── examples/             # Code samples and exercise data
└── resources/            # Curated links and further reading
```

## Quick Start

### 1. Use a Prompt Template

Browse [`prompts/`](./prompts/) for ready-to-use templates. Copy, customize, and paste into your AI tool.

```bash
# Example: Use the code review template
cat prompts/part2-patterns/ch05-code-review.md
```

### 2. Run a CLI Wrapper

The [`scripts/`](./scripts/) directory contains shell scripts that wrap common prompts:

```bash
# Review a file
./scripts/review.sh myfile.py python

# Generate tests
./scripts/test-gen.sh src/utils.py

# Explain code
./scripts/explain.sh complex-function.js
```

### 3. Set Up Agent Instructions

Copy templates from [`instruction-files/`](./instruction-files/) to your project:

```bash
# For Claude Code
cp instruction-files/CLAUDE.md.template ./CLAUDE.md

# For OpenAI Codex CLI
cp instruction-files/AGENTS.md.template ./AGENTS.md

# For GitHub Copilot
mkdir -p .github && cp instruction-files/copilot-instructions.md.template .github/copilot-instructions.md
```

Edit to match your project's conventions.

### 4. Build an MCP Server

The [`mcp/`](./mcp/) directory contains starter templates for building custom MCP servers:

```bash
# Python example
cd mcp/python-example
pip install -e .
python -m my_mcp_server

# TypeScript example
cd mcp/typescript-example
npm install
npm run build
```

## Directory Guide

### [`prompts/`](./prompts/)

Prompt templates organized by book part and chapter:

| Part | Focus | Key Templates |
|------|-------|---------------|
| Part 1 | Mindset | Contract-style prompts, verification checklists |
| Part 2 | Patterns | Building blocks, decomposition, review loops, multi-role |
| Part 3 | Workflows | Software engineering, DevOps, research, side projects |
| Part 4 | Beyond Chat | Evaluation frameworks, safety checklists |
| Part 5 | Tools | Tool-specific patterns for Copilot, Claude Code, Codex, MCP |

### [`scripts/`](./scripts/)

Shell scripts wrapping common AI tasks:

- `review.sh` - Code review with customizable criteria
- `explain.sh` - Code explanation for unfamiliar code
- `test-gen.sh` - Test case generation
- `debug.sh` - Debugging assistant setup
- `prompt-runner.py` - Generic prompt runner (Python)

### [`instruction-files/`](./instruction-files/)

Templates for AI agent instruction files:

- `CLAUDE.md.template` - For Claude Code
- `AGENTS.md.template` - For OpenAI Codex CLI
- `copilot-instructions.md.template` - For GitHub Copilot

### [`mcp/`](./mcp/)

Model Context Protocol server examples:

- `python-example/` - Simple MCP server in Python
- `typescript-example/` - Simple MCP server in TypeScript

### [`examples/`](./examples/)

Practice materials:

- `code-samples/` - Code to practice reviewing, explaining, testing
- `exercise-data/` - Data for book exercises
- `conversations/` - Example AI conversation transcripts

### [`resources/`](./resources/)

Curated links to documentation, papers, and tools.

## Usage Philosophy

These resources are **starting points, not solutions**. The book emphasizes:

1. **Customize for your context** - Edit templates to match your stack, conventions, and constraints
2. **Verify AI outputs** - Templates include verification steps; do not skip them
3. **Iterate and improve** - When a template does not work well, refine it
4. **Share what works** - Contributions welcome (see below)

## Contributing

Contributions welcome:

- **New templates** - Prompts that worked well for you
- **Bug fixes** - Corrections to existing content
- **Examples** - Additional code samples or exercise data
- **Translations** - Templates in other languages

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](./LICENSE)

## Links

- [The Book (LaTeX source)](https://github.com/Arthur742Ramos/AIBook)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [GitHub Copilot Documentation](https://docs.github.com/copilot)

---

*Companion to "The Developer's Guide to AI: Patterns, Tools, and Workflows"*
