# Depth-First Search (DFS)

## When to Use
- **Tree/graph traversal** where you need to explore all paths
- **Backtracking** problems (permutations, combinations, subsets)
- **Connected components**, cycle detection in graphs
- Keywords: "all paths", "connected", "traverse", "explore"

## Core Idea
Go as deep as possible before backtracking. Use recursion or an explicit stack.

## Templates

### DFS on Tree (Recursive)
```python
def dfs(node):
    if not node:
        return
    # process node (preorder)
    dfs(node.left)
    # process node (inorder)
    dfs(node.right)
    # process node (postorder)
```

### DFS on Graph
```python
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

### DFS on Grid
```python
def dfs(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if (r, c) in visited or grid[r][c] == 0:
        return
    visited.add((r, c))
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dfs(grid, r + dr, c + dc, visited)
```

### Iterative DFS (using stack)
```python
def dfs_iterative(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
```

## Complexity
- Time: O(V + E) for graphs, O(m * n) for grids
- Space: O(V) for recursion stack / visited set

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 94 | Binary Tree Inorder Traversal | Easy | Tree DFS | |
| 104 | Maximum Depth of Binary Tree | Easy | Tree DFS | |
| 112 | Path Sum | Easy | Tree DFS | |
| 200 | Number of Islands | Medium | Grid DFS | |
| 207 | Course Schedule | Medium | Cycle Detection | |
| 226 | Invert Binary Tree | Easy | Tree DFS | |
| 323 | Number of Connected Components | Medium | Graph DFS | |
| 543 | Diameter of Binary Tree | Easy | Tree DFS | |
| 695 | Max Area of Island | Medium | Grid DFS | |
| 733 | Flood Fill | Easy | Grid DFS | |

## Tips
- Recursive DFS can hit Python's recursion limit (~1000). Use iterative for deep graphs
- For tree problems, think about whether preorder, inorder, or postorder suits the problem
- DFS + memoization = top-down dynamic programming
