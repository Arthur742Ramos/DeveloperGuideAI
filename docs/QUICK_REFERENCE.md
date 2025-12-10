# AI Coding Tools Quick Reference

One-page reference for daily use. For details, see tool-specific guides.

---

## Which Tool When?

| Task | Tool |
|------|------|
| Quick completion in editor | GitHub Copilot |
| Explain code in current file | Copilot Chat |
| Multi-file refactoring | Claude Code or Codex |
| Debug with file access | Claude Code |
| Batch migrations | Codex CLI |
| Git operations | Claude Code |

---

## Universal Prompt Pattern

```
Role: [what expertise to apply]
Task: [what to do]
Context: [relevant background]
Constraints: [requirements and limits]
Output: [format wanted]
```

---

## Code Review Prompt

```
Review this code for production:
```[language]
[code]
```

Check: correctness, errors, performance, readability, security.
Rate each: GOOD / NEEDS WORK / PROBLEM
Be direct.
```

---

## Debug Prompt

```
Problem: [symptom]
Stack: [tech]
Tried: [attempts]

```
[error/logs]
```

Give: hypotheses, checks to run, likely fix.
```

---

## Test Generation Prompt

```
Generate tests for:
```[language]
[code]
```

Cover: normal cases, edge cases (empty, large, boundary), error cases.
```

---

## Instruction Files

| Tool | File | Location |
|------|------|----------|
| Claude Code | CLAUDE.md | Project root |
| Codex CLI | AGENTS.md | Project root |
| Copilot | copilot-instructions.md | .github/ |

### Minimal Template

```markdown
# Project

## Commands
- `npm run dev` - dev server
- `npm test` - tests

## Structure
- src/services/ - business logic
- src/routes/ - HTTP handlers

## Conventions
- [key convention]
- Pattern: see src/services/example.ts

## Do Not
- [constraint]
```

---

## Safety Checklist

Before pasting into AI:
- [ ] No API keys or secrets?
- [ ] No personal data?
- [ ] No internal URLs/IPs?
- [ ] No proprietary logic?

After getting output:
- [ ] Read the code?
- [ ] Tested it?
- [ ] Checked edge cases?
- [ ] Security review?

---

## Common Patterns

### Explain
```
Explain this code to someone who needs to modify it.
```

### Fix Error
```
Error: [message]
Code: [code]
What's wrong?
```

### Refactor
```
Refactor this to [goal]. Keep same interface.
```

### Add Feature
```
Add [feature] following patterns in [existing file].
```

---

## Keyboard Shortcuts

### Copilot (VS Code)
- Accept: Tab
- Reject: Esc
- Next suggestion: Alt+]
- Chat: Ctrl+I

### Claude Code / Codex
- Accept: Enter
- Reject: Esc
- Interrupt: Ctrl+C

---

## Red Flags in AI Output

Watch for:
- Hallucinated APIs or functions
- Outdated syntax or patterns
- Security issues (SQL injection, XSS)
- Missing error handling
- Wrong assumptions about your codebase

Always verify before using.

---

## Quick Evaluation

After using AI, ask:
- Did I finish faster than doing it manually?
- How much time fixing AI output?
- Was the quality acceptable?
- Would I use AI for this again?
