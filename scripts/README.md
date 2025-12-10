# CLI Wrapper Scripts

Shell scripts that wrap common AI prompts for quick command-line use.

## Setup

1. Add this directory to your PATH, or copy scripts to a directory in your PATH
2. Make scripts executable: `chmod +x *.sh`
3. Configure your AI CLI tool (see Configuration below)

## Available Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `review.sh` | Code review | `./review.sh file.py python` |
| `explain.sh` | Code explanation | `./explain.sh file.js` |
| `test-gen.sh` | Test generation | `./test-gen.sh src/utils.py` |
| `debug.sh` | Debugging assistant | `./debug.sh "error message"` |
| `prompt-runner.py` | Generic prompt runner | `./prompt-runner.py template.md file.py` |

## Configuration

These scripts use a generic `AI_CLI` variable. Set it to your preferred tool:

```bash
# For Claude Code
export AI_CLI="claude"

# For a generic OpenAI CLI
export AI_CLI="openai-cli"

# For a custom wrapper
export AI_CLI="my-ai-tool"
```

Or edit the scripts directly to use your tool.

## Script Details

### review.sh

Reviews code for production readiness.

```bash
./review.sh myfile.py python
./review.sh src/api/users.ts typescript
```

Checks: correctness, error handling, performance, readability, security.

### explain.sh

Explains what code does for someone unfamiliar with it.

```bash
./explain.sh complex-function.js
```

Covers: purpose, main steps, non-obvious parts, what would break if changed.

### test-gen.sh

Generates test cases for a function or module.

```bash
./test-gen.sh src/utils/parser.py
```

Generates: normal operation tests, edge cases, error cases.

### debug.sh

Sets up a debugging session with context.

```bash
./debug.sh "Connection refused when calling API"
```

Produces: hypotheses, diagnostic checks, suggested fixes.

### prompt-runner.py

Runs any prompt template against a file.

```bash
./prompt-runner.py ../prompts/part2-patterns/code-review.md myfile.py
```

Replaces `[FILE_CONTENT]` placeholder with file contents.

## Customization

Edit scripts to:
- Change the AI CLI command
- Add/remove review criteria
- Change output format
- Add project-specific context

## Limitations

- Scripts assume a CLI tool that accepts prompts via stdin or argument
- Adjust for your specific tool's interface
- These are starting points—customize for your workflow
