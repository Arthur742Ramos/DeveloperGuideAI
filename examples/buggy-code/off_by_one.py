"""
Off-by-one Error Example

This code has a classic off-by-one bug. Use AI debugging to find it.

Expected behavior: Process all items in the list
Actual behavior: Misses the last item

Exercise: Use the debugging prompt to identify and fix the issue.
"""


def process_items(items: list) -> list:
    """Process each item by doubling its value."""
    results = []

    # Bug: range goes from 0 to len-1, but we use i+1
    for i in range(len(items) - 1):
        results.append(items[i] * 2)

    return results


def find_max_pair_sum(numbers: list) -> int:
    """Find the maximum sum of any two adjacent numbers."""
    if len(numbers) < 2:
        return 0

    max_sum = numbers[0] + numbers[1]

    # Bug: should be len(numbers) - 1
    for i in range(1, len(numbers) - 2):
        pair_sum = numbers[i] + numbers[i + 1]
        if pair_sum > max_sum:
            max_sum = pair_sum

    return max_sum


def paginate(items: list, page_size: int, page: int) -> list:
    """Return a page of items (1-indexed pages)."""
    # Bug: off-by-one in start calculation for 1-indexed pages
    start = page * page_size
    end = start + page_size
    return items[start:end]


# Test cases that reveal the bugs
if __name__ == "__main__":
    # Test 1: process_items
    test_items = [1, 2, 3, 4, 5]
    result = process_items(test_items)
    print(f"process_items({test_items}) = {result}")
    print(f"Expected: [2, 4, 6, 8, 10], Got: {result}")
    print()

    # Test 2: find_max_pair_sum
    numbers = [1, 5, 2, 9, 3]  # Max pair is 9+3=12
    result = find_max_pair_sum(numbers)
    print(f"find_max_pair_sum({numbers}) = {result}")
    print(f"Expected: 12 (9+3), Got: {result}")
    print()

    # Test 3: paginate
    items = ["a", "b", "c", "d", "e", "f"]
    result = paginate(items, 2, 1)  # First page should be ["a", "b"]
    print(f"paginate(items, 2, 1) = {result}")
    print(f"Expected: ['a', 'b'], Got: {result}")
