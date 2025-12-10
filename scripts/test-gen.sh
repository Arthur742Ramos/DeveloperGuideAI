#!/bin/bash
# test-gen.sh - Test generation wrapper
# Usage: ./test-gen.sh <file> [framework]

set -e

FILE=$1
FRAMEWORK=${2:-"auto-detect"}

if [ -z "$FILE" ]; then
    echo "Usage: ./test-gen.sh <file> [framework]"
    echo "Example: ./test-gen.sh src/utils.py pytest"
    exit 1
fi

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found"
    exit 1
fi

# AI CLI command - customize for your tool
AI_CLI=${AI_CLI:-"echo 'Set AI_CLI environment variable to your AI CLI tool'"}

PROMPT=$(cat << 'EOF'
Given this code:

```
%FILE_CONTENT%
```

Generate test cases using %FRAMEWORK%. Cover:

1. **Normal operation** (3-5 cases)
   - Typical inputs with expected outputs

2. **Edge cases**
   - Empty input
   - Single element / minimal valid input
   - Very large input
   - Boundary values
   - Special characters / Unicode

3. **Error cases**
   - Invalid input types
   - Null/None/undefined values
   - Out-of-range values
   - Missing required fields

For each test:
- Descriptive name explaining what it tests
- Clear arrangement, action, assertion
- Brief comment on why this case matters

Output complete, runnable test code.
EOF
)

FILE_CONTENT=$(cat "$FILE")
PROMPT="${PROMPT//%FILE_CONTENT%/$FILE_CONTENT}"
PROMPT="${PROMPT//%FRAMEWORK%/$FRAMEWORK}"

echo "$PROMPT" | $AI_CLI
