#!/bin/bash
# debug.sh - Debugging assistant wrapper
# Usage: ./debug.sh "error message or symptom"

set -e

PROBLEM=$1

if [ -z "$PROBLEM" ]; then
    echo "Usage: ./debug.sh \"error message or symptom\""
    echo "Example: ./debug.sh \"Connection refused when calling API\""
    exit 1
fi

# AI CLI command - customize for your tool
AI_CLI=${AI_CLI:-"echo 'Set AI_CLI environment variable to your AI CLI tool'"}

PROMPT=$(cat << EOF
You are my debugging assistant.

Problem: $PROBLEM

Your tasks:
1. **Restate** the problem in your own words
2. **Hypotheses**: List 3-5 plausible causes, ranked by likelihood
3. **Diagnostics**: For each hypothesis, what evidence would confirm or rule it out?
4. **Checks**: Specific commands or queries to run for the top hypotheses
5. **Next step**: What should I try first?

Constraints:
- If you need more information, ask specific questions
- Separate "high confidence" suggestions from speculative ones
- State any assumptions about environment or versions
EOF
)

echo "$PROMPT" | $AI_CLI
