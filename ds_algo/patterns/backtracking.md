# Backtracking

## When to Use
- Generate **all** combinations, permutations, or subsets
- Constraint satisfaction (Sudoku, N-Queens)
- Decision trees where you need to explore and undo choices
- Keywords: "all possible", "generate", "combinations", "permutations", "subsets"

## Core Idea
Build a solution incrementally. At each step, make a choice, recurse, then **undo the choice** (backtrack) to explore other options.

## Template
```python
def backtrack(candidates, path, result, start):
    if is_valid_solution(path):
        result.append(path[:])  # copy the path
        return

    for i in range(start, len(candidates)):
        # skip duplicates if needed
        if i > start and candidates[i] == candidates[i - 1]:
            continue

        path.append(candidates[i])      # choose
        backtrack(candidates, path, result, i + 1)  # explore
        path.pop()                        # un-choose (backtrack)
```

## Variants

### Subsets
```python
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result
```

### Permutations
```python
def permutations(nums):
    result = []
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    backtrack([], [False] * len(nums))
    return result
```

### Combination Sum (reuse allowed)
```python
def combination_sum(candidates, target):
    result = []
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # i, not i+1 (reuse)
            path.pop()
    candidates.sort()
    backtrack(0, [], target)
    return result
```

## Complexity
- Time: O(2^n) for subsets, O(n!) for permutations
- Space: O(n) recursion depth

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 17 | Letter Combinations of a Phone Number | Medium | Combinations | |
| 22 | Generate Parentheses | Medium | Constraint | |
| 39 | Combination Sum | Medium | Reuse allowed | |
| 40 | Combination Sum II | Medium | No reuse + dedup | |
| 46 | Permutations | Medium | Permutation | |
| 47 | Permutations II | Medium | Dedup | |
| 51 | N-Queens | Hard | Constraint | |
| 78 | Subsets | Medium | Subsets | |
| 79 | Word Search | Medium | Grid backtrack | |
| 90 | Subsets II | Medium | Dedup subsets | |
| 131 | Palindrome Partitioning | Medium | Partition | |

## Tips
- Sort input first to easily skip duplicates
- Always **copy** the path when adding to result (`path[:]` not `path`)
- Pruning early (skipping invalid branches) is key to performance
