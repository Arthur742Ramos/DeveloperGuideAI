# ReAct Pattern Template

## Purpose

Reasoning + Acting pattern for tool-using AI agents. From Chapter 8.

## The Pattern

```
Thought → Action → Observation → Thought → Action → ...
```

## Basic ReAct Prompt

```
You have access to these tools:
- search(query): Search documentation
- read_file(path): Read a file's contents
- run_test(name): Run a specific test
- [add your tools]

To investigate [problem]:

Think step by step. For each step:
1. State what you are thinking
2. Choose an action and explain why
3. Report what you observed
4. Decide next steps

Continue until you have a conclusion or solution.
```

## Tool Usage Guidance

```
Guidelines for using tools:

- Use search() when you need current information or are unsure about facts
- Use read_file() to examine code before modifying it
- Do NOT guess file contents—always read first
- Do NOT make destructive changes without explicit approval

Before each action, state why you're taking it.
After each observation, state what you learned.
```

## Safety Boundaries

```
You may:
- Read any file in the src/ directory
- Run tests
- Search documentation

You may NOT:
- Modify files without explicit approval
- Make network requests outside the test environment
- Delete anything
- Run commands with sudo

If you need to do something not on the "may" list, ask first.
```

## Requiring Approval

```
Before executing any command that modifies files or makes external requests:

1. Show me the exact command
2. Explain what it will do
3. Explain what could go wrong
4. Wait for my explicit "proceed" before executing

Never assume approval.
```

## Example: Debugging Investigation

```
You have access to:
- read_file(path): Read file contents
- grep(pattern, path): Search for pattern
- run_test(name): Run a specific test
- git_diff(): Show recent changes

The test_user_creation test is failing with a timeout.

Investigate why. For each step:
- Thought: What are you trying to learn?
- Action: What tool will you use and why?
- Observation: What did you find?

Continue until you identify the root cause.
```

### Expected Agent Behavior

```
Thought: I should first read the failing test to understand what it does.

Action: read_file("tests/test_user.py")

Observation: The test creates a user, waits for email confirmation,
then verifies the user is active. There's a 30-second timeout.

Thought: The timeout could be in email sending or waiting.
Let me check the email configuration.

Action: read_file("config/test.py")

Observation: Email is configured to use a real SMTP server in tests.

Thought: That's suspicious. Let me check if CI has network access.

Action: read_file(".github/workflows/test.yml")

Observation: CI runs in an isolated network without external access.

Conclusion: The test times out because CI can't reach the SMTP server.
The fix is to mock the email service in tests.
```

## Dry Run Mode

For high-risk operations, use dry run:

```
Show me what you would do, but do not execute.

For each action:
1. The command you would run
2. What you expect to happen
3. What could go wrong

I will review and approve before actual execution.
```

## When to Use ReAct

| Situation | Use ReAct? |
|-----------|------------|
| Simple question | No |
| Multi-step investigation | Yes |
| Tool-using task | Yes |
| High-risk operations | Yes (with approval gates) |
| Autonomous agent work | Yes |
