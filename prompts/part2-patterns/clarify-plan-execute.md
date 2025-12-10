# Clarify-Plan-Execute Template

## Purpose

The most reliable pattern for complex tasks. Prevents AI from running in the wrong direction. From Chapter 6.

## Phase 1: Clarify

```
I need help with: [brief description of goal]

Before proposing solutions, ask me up to [5-7] clarifying questions about:
- Current architecture and constraints
- Requirements and priorities
- What has been tried before
- Success criteria

Ask only the questions that would most change your recommendation.
```

## Phase 2: Plan

```
Based on my answers, propose a plan:

1. Main components or steps needed
2. Key decisions to make
3. Risks and how to mitigate them
4. Suggested order of implementation

Do NOT write code yet. I want to review the plan first.
```

## Phase 3: Execute

```
The plan looks good. Now implement [specific step]:

Include:
- The actual code/output
- Brief comments explaining non-obvious decisions
- One example of how to use it

Stop after this step so I can review before continuing.
```

## Full Conversation Flow

### Turn 1: Clarify

**You:**
```
I need to add authentication to our API.

Before suggesting anything, ask me clarifying questions about:
- Current setup and constraints
- User requirements
- Security needs
- Integration requirements

Max 7 questions, focused on what would change your recommendation.
```

**AI asks questions...**

### Turn 2: Answer and Request Plan

**You:**
```
[Answer the questions]

Now propose a plan for implementing authentication:
- Main approach
- Components needed
- Order of implementation
- Key risks

Don't write code yet.
```

**AI proposes plan...**

### Turn 3: Approve and Execute First Step

**You:**
```
Good plan. Let's modify step 2 to [adjustment].

Now implement step 1 only: [specific description]

Stop after this step for review.
```

### Turn 4+: Continue or Adjust

**You:**
```
Step 1 looks good. Proceed to step 2.
```

or

```
Issue with step 1: [description].
Let's revise before continuing.
```

## When to Use

| Situation | Use Clarify-Plan-Execute? |
|-----------|---------------------------|
| Simple, well-defined task | No, just ask directly |
| Complex, multi-step work | Yes |
| Uncertain requirements | Yes (emphasize clarify phase) |
| High-risk changes | Yes (add approval gates) |
| Learning new domain | Yes (clarify reveals knowledge gaps) |

## Shortcuts for Simpler Tasks

### Plan-Execute (Skip Clarify)

When requirements are clear:

```
I need to: [clear requirement]

Context:
- [constraint 1]
- [constraint 2]

Propose a brief plan (3-5 steps), then implement step 1.
```

### Execute with Checkpoints

When planning is overkill but you want review points:

```
Implement [task].

After each major component, pause and show me:
- What you just did
- What you'll do next
- Any concerns

Wait for my "continue" before proceeding.
```
