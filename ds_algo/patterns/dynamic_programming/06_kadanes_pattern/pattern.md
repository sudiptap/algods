# Kadane's Pattern

## Core Idea
At each position, decide: extend the current subarray or start fresh.

## Template
```python
def max_subarray(nums):
    curr_max = global_max = nums[0]
    for num in nums[1:]:
        curr_max = max(num, curr_max + num)
        global_max = max(global_max, curr_max)
    return global_max
```

## Complexity
- Time: O(n)
- Space: O(1)

## Classic Problems
- 53. Maximum Subarray
- 152. Maximum Product Subarray
- 918. Maximum Sum Circular Subarray
- 1186. Maximum Subarray Sum with One Deletion
