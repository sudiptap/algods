# Monotonic Stack

## When to Use
- Finding the **next greater/smaller element** for each element
- Problems involving spans, stock prices, temperatures
- Histogram-based problems
- Keywords: "next greater", "next smaller", "daily temperatures", "histogram"

## Core Idea
Maintain a stack that is always sorted (increasing or decreasing). When a new element violates the order, pop elements and process them.

## Templates

### Next Greater Element
```python
def next_greater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result
```

### Next Smaller Element
```python
def next_smaller(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result
```

### Largest Rectangle in Histogram
```python
def largest_rectangle(heights):
    stack = []
    max_area = 0

    for i, h in enumerate(heights + [0]):  # sentinel
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area
```

## Complexity
- Time: O(n) — each element pushed/popped at most once
- Space: O(n)

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 42 | Trapping Rain Water | Hard | Monotonic stack | |
| 84 | Largest Rectangle in Histogram | Hard | Decreasing stack | |
| 85 | Maximal Rectangle | Hard | Histogram per row | |
| 496 | Next Greater Element I | Easy | Decreasing stack | |
| 503 | Next Greater Element II | Medium | Circular array | |
| 739 | Daily Temperatures | Medium | Decreasing stack | |
| 901 | Online Stock Span | Medium | Decreasing stack | |
| 907 | Sum of Subarray Minimums | Medium | Increasing stack | |

## Tips
- Store **indices** in the stack, not values (you can always look up the value)
- For circular arrays, iterate `2n` times using `i % n`
- Decreasing stack for "next greater", increasing stack for "next smaller"
