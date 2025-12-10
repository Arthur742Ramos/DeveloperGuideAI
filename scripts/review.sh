#!/bin/bash
# review.sh - Code review wrapper
# Usage: ./review.sh <file> [language]

set -e

FILE=$1
LANGUAGE=${2:-"auto-detect"}

if [ -z "$FILE" ]; then
    echo "Usage: ./review.sh <file> [language]"
    echo "Example: ./review.sh myfile.py python"
    exit 1
fi

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found"
    exit 1
fi

# AI CLI command - customize for your tool
AI_CLI=${AI_CLI:-"echo 'Set AI_CLI environment variable to your AI CLI tool'"}

PROMPT=$(cat << 'EOF'
You are a senior engineer reviewing this code for production readiness.

Language: %LANGUAGE%

```
%FILE_CONTENT%
```

Evaluate against these criteria:

1. **Correctness**: Does it do what it claims?
2. **Error handling**: Are failure cases covered?
3. **Performance**: Any obvious inefficiencies?
4. **Readability**: Could a new team member understand this?
5. **Security**: Any potential vulnerabilities?

For each criterion:
- Rating: GOOD / NEEDS WORK / PROBLEM
- Specific feedback with line numbers if applicable
- Suggested fix if there's a problem

Be direct about issues. Honest assessment, not encouragement.
EOF
)

FILE_CONTENT=$(cat "$FILE")

# Replace placeholders
PROMPT="${PROMPT//%LANGUAGE%/$LANGUAGE}"
PROMPT="${PROMPT//%FILE_CONTENT%/$FILE_CONTENT}"

# Run the AI CLI
echo "$PROMPT" | $AI_CLI
