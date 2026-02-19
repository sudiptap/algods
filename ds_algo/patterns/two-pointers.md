# Two Pointers

## When to Use
- **Sorted arrays** where you need to find pairs/triplets satisfying a condition
- **Opposite ends** converging toward the middle
- Removing duplicates, partitioning arrays
- Keywords: "sorted", "pair", "triplet", "in-place", "two sum"

## Core Idea
Use two pointers to traverse the data structure from different positions. Movement decisions narrow the search space efficiently.

## Variants

### Opposite Direction (Converging)
Start one pointer at the beginning, one at the end, and move inward.

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### Same Direction (Fast & Slow)
Both pointers move in the same direction at different speeds.

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

### Three Pointers (3Sum pattern)
Fix one element, then use two pointers on the rest.

```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicates
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
```

## Complexity
- Time: O(n) for two pointers, O(n^2) for 3Sum
- Space: O(1) extra space (in-place)

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 1 | Two Sum (sorted variant) | Easy | Converging | |
| 11 | Container With Most Water | Medium | Converging | |
| 15 | 3Sum | Medium | Three Pointers | |
| 26 | Remove Duplicates from Sorted Array | Easy | Fast & Slow | |
| 42 | Trapping Rain Water | Hard | Converging | |
| 75 | Sort Colors | Medium | Three-way partition | |
| 125 | Valid Palindrome | Easy | Converging | |
| 167 | Two Sum II | Medium | Converging | |
| 283 | Move Zeroes | Easy | Fast & Slow | |
| 977 | Squares of a Sorted Array | Easy | Converging | |

## Tips
- Always check if the array needs to be **sorted first**
- Skip duplicates to avoid duplicate results (common follow-up)
- Converging pointers work because moving one pointer strictly reduces the search space
