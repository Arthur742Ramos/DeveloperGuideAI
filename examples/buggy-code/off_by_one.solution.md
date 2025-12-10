# Solution: Off-by-One Errors

## Bug 1: `process_items`

**Problem**: Loop iterates `len(items) - 1` times, missing the last item.

```python
# Buggy
for i in range(len(items) - 1):

# Fixed
for i in range(len(items)):
```

**Better fix**: Use direct iteration
```python
for item in items:
    results.append(item * 2)
```

## Bug 2: `find_max_pair_sum`

**Problem**: Loop stops at `len(numbers) - 2`, missing the last pair.

```python
# Buggy
for i in range(1, len(numbers) - 2):

# Fixed
for i in range(1, len(numbers) - 1):
```

## Bug 3: `paginate`

**Problem**: Using 0-indexed math for 1-indexed pages.

```python
# Buggy (page 1 returns items 2-3 instead of 0-1)
start = page * page_size

# Fixed
start = (page - 1) * page_size
```

## Lessons

1. **Be explicit about indexing**: Comments should clarify if indices are 0 or 1-based
2. **Prefer iteration over indexing**: `for item in items` avoids index bugs
3. **Test boundary cases**: First item, last item, single item, empty list
4. **Draw it out**: Sketch indices on paper for complex loops

## AI Debugging Tips

When debugging off-by-one errors with AI:

1. Provide concrete test cases with expected vs actual output
2. Ask for a trace through the loop iterations
3. Request boundary case analysis
