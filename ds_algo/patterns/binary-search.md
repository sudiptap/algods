# Binary Search

## When to Use
- **Sorted** arrays or search spaces
- Finding a boundary (first/last element satisfying a condition)
- Minimizing/maximizing a value where the answer space is monotonic
- Keywords: "sorted", "find minimum", "search", "rotated"

## Core Idea
Repeatedly halve the search space. If you can define a condition that splits the space into YES/NO halves, binary search applies.

## Variants

### Standard Binary Search
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Find Left Boundary (First Occurrence)
```python
def find_left(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            if nums[mid] == target:
                result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
```

### Binary Search on Answer (Minimize/Maximize)
```python
def binary_search_on_answer(lo, hi):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if condition(mid):
            hi = mid  # mid might be the answer, search left
        else:
            lo = mid + 1  # mid is too small
    return lo
```

## Complexity
- Time: O(log n)
- Space: O(1)

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 33 | Search in Rotated Sorted Array | Medium | Modified | |
| 34 | Find First and Last Position | Medium | Boundary | |
| 35 | Search Insert Position | Easy | Standard | |
| 69 | Sqrt(x) | Easy | On Answer | |
| 74 | Search a 2D Matrix | Medium | Standard | |
| 153 | Find Minimum in Rotated Sorted Array | Medium | Modified | |
| 278 | First Bad Version | Easy | Boundary | |
| 410 | Split Array Largest Sum | Hard | On Answer | |
| 704 | Binary Search | Easy | Standard | |
| 875 | Koko Eating Bananas | Medium | On Answer | |
| 1011 | Capacity To Ship Packages | Medium | On Answer | |

## Tips
- Use `left + (right - left) // 2` to avoid integer overflow
- "Binary search on answer" is powerful: if you can verify a candidate answer in O(n), the whole solution is O(n log n)
- For rotated arrays, one half is always sorted — use that to decide which half to search
