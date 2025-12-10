# Runbook Generation Template

## Purpose

Capture operational knowledge after debugging or implementing infrastructure. From Chapter 11.

## The Prompt

```
We just [debugged an issue / implemented a system] where [brief description].

The [root cause / key mechanism] was [explanation].

Write a runbook that a future on-call engineer could follow:

1. **Recognition**: How to identify this problem
   - Symptoms and alerts
   - What distinguishes this from similar issues

2. **Diagnosis**: Step-by-step commands
   - Each command should be copy-paste ready
   - Include expected output examples

3. **Resolution**: The fix
   - Step-by-step procedure
   - Safety checks before each step
   - Rollback procedure if something goes wrong

4. **Verification**: How to confirm the fix worked
   - What to check
   - Expected values

5. **Escalation**: When to escalate instead
   - Signs this is a bigger problem
   - Who to contact

Keep it concise and copy-paste friendly.
```

## Quick Runbook (Simple Issues)

```
Document this operational procedure:

Task: [what needs to be done]
When: [triggers or schedule]

Steps:
1. [step 1]
2. [step 2]
3. [step 3]

Format as a runbook with commands I can copy-paste.
```

## Incident Postmortem to Runbook

```
Here's our incident postmortem:

[paste postmortem or summary]

Generate a runbook to prevent/quickly resolve similar incidents:
- Detection
- Diagnosis
- Resolution
- Prevention checks
```

## IaC Change Runbook

```
Document this infrastructure change:

Change: [description]
Environment: [where]
Dependencies: [what else this affects]

Generate runbook covering:
1. Pre-flight checks
2. The change procedure
3. Verification steps
4. Rollback procedure
5. Post-change monitoring
```

## Example: Database Connection Issue

```
We debugged an issue where the API started returning 500 errors due to
database connection pool exhaustion.

Root cause: A background job was not releasing connections properly.

Write a runbook covering:
1. How to recognize connection pool exhaustion
2. Commands to check current connections
3. Emergency mitigation (restart vs. fix)
4. The proper fix
5. How to verify resolution
6. When to escalate to DBA
```
