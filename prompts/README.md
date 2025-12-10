# Prompt Templates

Ready-to-use prompt templates organized by topic. Copy, customize for your context, and use with any AI assistant.

## How to Use

1. **Find the right template** - Browse by part/chapter or use the index below
2. **Copy the prompt** - Use the text in "The Prompt" section
3. **Customize** - Replace bracketed placeholders with your specifics
4. **Verify output** - Follow the verification steps in each template

## Template Index

### Part 1: The Mindset Shift

| Template | Purpose |
|----------|---------|
| [Contract-Style Prompt](part1-mindset/contract-style-prompt.md) | Structure any request clearly |
| [Verification Checklist](part1-mindset/verification-checklist.md) | Systematic output verification |
| [Conversation Management](part1-mindset/conversation-management.md) | Reset, summarize, branch techniques |
| [Uncertainty Signals](part1-mindset/uncertainty-signals.md) | Request confidence indicators |

### Part 2: Prompt Patterns That Scale

| Template | Purpose |
|----------|---------|
| [Building Blocks](part2-patterns/building-blocks.md) | Role, constraints, examples, steps |
| [Code Review](part2-patterns/code-review.md) | Production-ready code review |
| [Clarify-Plan-Execute](part2-patterns/clarify-plan-execute.md) | Complex task decomposition |
| [Review Loop](part2-patterns/review-loop.md) | Generate-review-revise cycle |
| [Multi-Role Workflow](part2-patterns/multi-role.md) | Architect, Coder, Tester, Explainer |
| [ReAct Pattern](part2-patterns/react-pattern.md) | Reasoning + Acting for agents |

### Part 3: Real Workflows

| Template | Purpose |
|----------|---------|
| [Code Generation](part3-workflows/code-generation.md) | Context-rich code generation |
| [Test Generation](part3-workflows/test-generation.md) | Comprehensive test cases |
| [Debugging Assistant](part3-workflows/debugging.md) | Systematic debugging |
| [Runbook Generation](part3-workflows/runbook.md) | Capture operational knowledge |
| [Paper Summarization](part3-workflows/paper-summary.md) | Research paper analysis |
| [MVP Scoping](part3-workflows/mvp-scoping.md) | Side project planning |

### Part 4: Beyond the Chat Box

| Template | Purpose |
|----------|---------|
| [Effectiveness Evaluation](part4-beyond/evaluation.md) | Is AI actually helping? |
| [Data Safety Checklist](part4-beyond/data-safety.md) | What not to share |
| [Anonymization Guide](part4-beyond/anonymization.md) | Safe problem descriptions |

### Part 5: AI Coding Tools

| Template | Purpose |
|----------|---------|
| [Copilot Patterns](part5-tools/copilot-patterns.md) | IDE-integrated completion |
| [Claude Code Patterns](part5-tools/claude-code-patterns.md) | Terminal agent tasks |
| [Codex CLI Patterns](part5-tools/codex-patterns.md) | Approval mode workflows |
| [MCP Tool Design](part5-tools/mcp-tool-design.md) | Custom tool descriptions |

## Customization Tips

### Replace Placeholders

Templates use `[BRACKETS]` for values you must provide:

```
Language: [YOUR LANGUAGE]
Framework: [YOUR FRAMEWORK]
```

### Add Context

The more relevant context you provide, the better the output:

```
# Instead of:
Review this code.

# Use:
Review this code. It's part of our payment processing system.
The function handles webhook verification from Stripe.
We use Python 3.11 with FastAPI.
```

### Adjust Constraints

Modify constraints to match your needs:

```
# Original template:
- Maximum 500 words

# Your version:
- Maximum 200 words (for quick review)
# or
- As detailed as needed (for thorough analysis)
```

## Contributing New Templates

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines on submitting new templates.
