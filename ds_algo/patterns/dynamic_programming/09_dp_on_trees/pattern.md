# DP on Trees

## Core Idea
Use post-order traversal (solve children first), then combine results at each node.

## Template
```python
def tree_dp(root):
    def dfs(node):
        if not node:
            return base_case
        left = dfs(node.left)
        right = dfs(node.right)
        # update global answer
        nonlocal ans
        ans = max(ans, combine(left, right, node.val))
        # return value for parent
        return best_single_path(left, right, node.val)

    ans = float('-inf')
    dfs(root)
    return ans
```

## Complexity
- Time: O(n) — visit each node once
- Space: O(h) — recursion stack

## Classic Problems
- 124. Binary Tree Maximum Path Sum
- 337. House Robber III
- 543. Diameter of Binary Tree
- 968. Binary Tree Cameras
