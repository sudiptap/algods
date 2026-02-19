# Graph - Topological Sort

## When to Use
- **Ordering with dependencies** (course prerequisites, build systems)
- **Directed Acyclic Graph (DAG)** processing
- Detecting cycles in directed graphs
- Keywords: "prerequisites", "order", "schedule", "dependency"

## Core Idea
Process nodes in an order such that every node comes after all its dependencies. Only possible for DAGs.

## Templates

### Kahn's Algorithm (BFS - Indegree)
```python
from collections import deque, defaultdict

def topological_sort(num_nodes, edges):
    graph = defaultdict(list)
    indegree = [0] * num_nodes

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(num_nodes) if indegree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) == num_nodes:
        return order  # valid topological order
    return []  # cycle detected
```

### DFS-based Topological Sort
```python
def topological_sort_dfs(num_nodes, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_nodes
    order = []
    has_cycle = False

    def dfs(node):
        nonlocal has_cycle
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                has_cycle = True
                return
            if color[neighbor] == WHITE:
                dfs(neighbor)
        color[node] = BLACK
        order.append(node)

    for i in range(num_nodes):
        if color[i] == WHITE:
            dfs(i)

    if has_cycle:
        return []
    return order[::-1]
```

## Complexity
- Time: O(V + E)
- Space: O(V + E)

## Classic Problems
| # | Problem | Difficulty | Variant | Status |
|---|---------|-----------|---------|--------|
| 207 | Course Schedule | Medium | Cycle Detection | |
| 210 | Course Schedule II | Medium | Topo Sort | |
| 269 | Alien Dictionary | Hard | Build + Sort | |
| 310 | Minimum Height Trees | Medium | Leaf removal | |
| 802 | Find Eventual Safe States | Medium | Reverse graph | |
| 1462 | Course Schedule IV | Medium | Transitive closure | |

## Tips
- Kahn's is generally easier to implement and debug
- If `len(order) < num_nodes`, a cycle exists
- For "all valid orderings", use backtracking with indegree tracking
