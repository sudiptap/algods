# Sliding Window

## When to Use
- Problems involving **contiguous subarrays or substrings**
- Asked to find min/max/longest/shortest subarray meeting a condition
- Keywords: "subarray", "substring", "contiguous", "window"

## Core Idea
Maintain a window `[left, right]` over the array. Expand `right` to include elements, shrink `left` to maintain constraints. Avoid recomputing from scratch each time.

## Two Variants

### Fixed-Size Window
Window size `k` is given. Slide it across the array.

```python
def fixed_window(nums, k):
    window_sum = sum(nums[:k])
    result = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        result = max(result, window_sum)
    return result
```

### Variable-Size Window
Find the optimal window size that satisfies a condition.

```python
def variable_window(s):
    left = 0
    window = {}  # or any state tracking
    result = 0
    for right in range(len(s)):
        # expand: add s[right] to window state
        while window_is_invalid():
            # shrink: remove s[left] from window state
            left += 1
        result = max(result, right - left + 1)
    return result
```

## Complexity
- Time: O(n) — each element is added/removed from window at most once
- Space: O(k) or O(1) depending on state tracked

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 3 | Longest Substring Without Repeating Characters | Medium | Variable | |
| 76 | Minimum Window Substring | Hard | Variable | |
| 209 | Minimum Size Subarray Sum | Medium | Variable | |
| 239 | Sliding Window Maximum | Hard | Fixed + Deque | |
| 424 | Longest Repeating Character Replacement | Medium | Variable | |
| 567 | Permutation in String | Medium | Fixed | |
| 904 | Fruit Into Baskets | Medium | Variable | |
| 1004 | Max Consecutive Ones III | Medium | Variable | |

## Tips
- Variable window: think about what makes the window **invalid** and shrink from the left
- Use a hashmap/counter to track window contents for string problems
- For fixed window: remember to subtract the outgoing element and add the incoming one
