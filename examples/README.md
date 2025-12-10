# Example Code and Exercise Data

Practice materials for exercises in "The Developer's Guide to AI."

## Directory Structure

```
examples/
├── buggy-code/        # Intentionally buggy code for debugging practice
├── review-targets/    # Code samples for review exercises
├── refactoring/       # Code to refactor with AI assistance
└── data/              # Synthetic data for anonymization exercises
```

## Using These Examples

### Debugging Practice (Chapter 11)

The `buggy-code/` directory contains intentionally buggy implementations:

```bash
# Try debugging with AI
./scripts/debug.sh "TypeError in user authentication"

# Or use the prompt template
cat prompts/part3-workflows/debugging.md
```

Each buggy file has a corresponding `.solution.md` explaining the bug.

### Code Review Practice (Chapter 9)

Use `review-targets/` with the review prompts:

```bash
./scripts/review.sh examples/review-targets/api_endpoint.py Python
```

### Anonymization Practice (Chapter 14)

The `data/` directory contains synthetic "sensitive" data for practicing anonymization techniques before using real data with AI.

## File Index

### buggy-code/
| File | Bug Type | Difficulty |
|------|----------|------------|
| `off_by_one.py` | Off-by-one error | Easy |
| `race_condition.js` | Race condition | Medium |
| `null_reference.ts` | Null handling | Easy |
| `memory_leak.py` | Resource leak | Medium |
| `sql_injection.py` | Security vulnerability | Medium |

### review-targets/
| File | Review Focus |
|------|--------------|
| `api_endpoint.py` | REST API patterns |
| `data_processor.ts` | Error handling |
| `auth_middleware.js` | Security review |

### data/
| File | Purpose |
|------|---------|
| `sample_users.json` | User data anonymization |
| `sample_logs.txt` | Log sanitization |
| `sample_config.env` | Secret redaction |
