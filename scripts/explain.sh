#!/bin/bash
# explain.sh - Code explanation wrapper
# Usage: ./explain.sh <file>

set -e

FILE=$1

if [ -z "$FILE" ]; then
    echo "Usage: ./explain.sh <file>"
    echo "Example: ./explain.sh complex-function.js"
    exit 1
fi

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found"
    exit 1
fi

# AI CLI command - customize for your tool
AI_CLI=${AI_CLI:-"echo 'Set AI_CLI environment variable to your AI CLI tool'"}

PROMPT=$(cat << 'EOF'
Explain this code as if I'm a developer who needs to modify it:

```
%FILE_CONTENT%
```

Cover:
1. **High-level purpose**: What is this code for? (1-2 sentences)
2. **Main steps**: Walk through the logic in order
3. **Non-obvious parts**: What's tricky or easy to misunderstand?
4. **Dependencies**: What does this rely on?
5. **Modification risks**: What would break if I changed X?

Don't just repeat the code in English. Explain the intent and gotchas.
EOF
)

FILE_CONTENT=$(cat "$FILE")
PROMPT="${PROMPT//%FILE_CONTENT%/$FILE_CONTENT}"

echo "$PROMPT" | $AI_CLI
