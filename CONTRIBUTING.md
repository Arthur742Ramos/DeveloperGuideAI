# Contributing to DeveloperGuideAI

Thank you for your interest in contributing! This repository provides practical resources for AI-assisted development and benefits from community improvements.

## Ways to Contribute

### 1. New Prompt Templates

Have a prompt pattern that works well? Add it!

**Guidelines:**
- Place in the appropriate `prompts/partX-*/` directory
- Use the existing template format (see below)
- Include: purpose, the prompt itself, usage notes, and variations
- Test with at least two different AI tools before submitting

**Template format:**
```markdown
# [Descriptive Name]

## Purpose
[1-2 sentences on what this prompt accomplishes]

## The Prompt
```
[The actual prompt text]
```

## Usage Notes
- [When to use this]
- [What to customize]
- [What to verify in the output]

## Variations
- [Alternative versions for different contexts]
```

### 2. Script Improvements

The `scripts/` directory contains CLI wrappers. Improvements welcome:

- Bug fixes
- New scripts for common tasks
- Better error handling
- Cross-platform compatibility (bash/zsh/PowerShell)

### 3. MCP Server Examples

Have a useful MCP server pattern? Add it to `mcp/`:

- Keep examples minimal and focused
- Include clear documentation
- Follow the existing structure

### 4. Code Samples and Exercise Data

Add to `examples/`:

- Code samples for practicing AI-assisted review/explanation/testing
- Exercise data for practicing AI-assisted workflows
- Example conversation transcripts showing patterns in action

### 5. Resource Links

Found a great resource? Add it to `resources/README.md`:

- Documentation links
- Blog posts with practical patterns
- Tools and utilities
- Research papers

## Submission Process

1. **Fork** the repository
2. **Create a branch** for your changes (`git checkout -b add-new-template`)
3. **Make your changes** following the guidelines above
4. **Test** your additions (prompts should work, scripts should run)
5. **Submit a Pull Request** with a clear description

## Code of Conduct

- Be respectful and constructive
- Focus on practical, tested contributions
- Credit sources when adapting others' work
- Keep content appropriate for professional use

## Questions?

Open an issue if you're unsure whether something fits or need guidance on format.

---

Thank you for helping make this resource better for everyone!
