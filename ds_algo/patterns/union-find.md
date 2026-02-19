# Union-Find (Disjoint Set Union)

## When to Use
- **Grouping / connectivity** problems
- Determining if two elements are in the same component
- Counting connected components
- Keywords: "connected", "groups", "union", "same component", "redundant connection"

## Core Idea
Maintain a forest of trees where each tree represents a connected component. Two operations: `find` (which component?) and `union` (merge two components).

## Template
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # number of components

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already connected
        # union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.count -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

## Complexity
- Find/Union: O(alpha(n)) ~ nearly O(1) with path compression + union by rank
- Space: O(n)

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 128 | Longest Consecutive Sequence | Medium | Grouping | |
| 200 | Number of Islands | Medium | Grid components | |
| 261 | Graph Valid Tree | Medium | Connectivity | |
| 305 | Number of Islands II | Hard | Dynamic connectivity | |
| 323 | Number of Connected Components | Medium | Count components | |
| 547 | Number of Provinces | Medium | Count components | |
| 684 | Redundant Connection | Medium | Cycle detection | |
| 721 | Accounts Merge | Medium | Merge groups | |
| 990 | Satisfiability of Equality Equations | Medium | Grouping | |

## Tips
- Path compression + union by rank together give near-constant time operations
- Union-Find vs BFS/DFS: Union-Find is better when connections are added incrementally
- For grids, convert `(row, col)` to a 1D index: `row * cols + col`
