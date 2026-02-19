# Breadth-First Search (BFS)

## When to Use
- **Shortest path** in unweighted graphs
- **Level-order traversal** of trees
- Exploring neighbors first before going deeper
- Keywords: "shortest", "level order", "nearest", "minimum steps"

## Core Idea
Use a queue. Process nodes level by level. First time you reach a node is the shortest path.

## Templates

### BFS on Graph
```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### BFS with Level Tracking
```python
def bfs_levels(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

### BFS on Grid (Shortest Path)
```python
def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0, 0)])  # (row, col, distance)
    visited = {(0, 0)}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, dist = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    return -1
```

## Complexity
- Time: O(V + E) for graphs, O(m * n) for grids
- Space: O(V) for the queue

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 102 | Binary Tree Level Order Traversal | Medium | Tree BFS | |
| 127 | Word Ladder | Hard | Graph BFS | |
| 199 | Binary Tree Right Side View | Medium | Tree BFS | |
| 200 | Number of Islands | Medium | Grid BFS | |
| 286 | Walls and Gates | Medium | Multi-source BFS | |
| 542 | 01 Matrix | Medium | Multi-source BFS | |
| 752 | Open the Lock | Medium | Graph BFS | |
| 994 | Rotting Oranges | Medium | Multi-source BFS | |
| 1091 | Shortest Path in Binary Matrix | Medium | Grid BFS | |

## Tips
- BFS guarantees shortest path in **unweighted** graphs
- Multi-source BFS: start with all sources in the queue at once
- Always mark visited **before** adding to queue (not when popping) to avoid duplicates
