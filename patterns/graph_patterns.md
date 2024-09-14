## Graph Patterns
### basic DFS
```
def hasCycle(graph, curr_node, visited, parent_node):
    visited.add(curr_node)
    for next_node in graph[curr_node]:
        if next_node == parent_node:
            continue
        if next_node in visited:
            return True
        if hasCycle(graph, next_node, visited, curr_node):
            return True
    return False

for curr_node in len(range(nodes)):
    if curr_node not in visited and hasCycle(graph, curr_node, visited, -1):
        return True
return False
```
### basic BFS
```
```
### Cycle detection in undirected graph using DFS
```
def hasCycle(graph, curr_node, visited, in_rec):
    visited.add(curr_node)
    in_rec.add(curr_node)

    for next_node in graph[curr_node]:
        if next_node in visited and hasCycle(graph, next_node, visited, in_rec):
            return True
        else if(next_node in in_rec):
            return True
    
    in_rec.delete(curr_node)
    return False

visited = set()
in_rec = set()
for curr_node in range(len(nodes)):
    if curr_node not in visited and hasCycle(graph, curr_node, visited, in_rec):
        return True
return False
```
### Cycle detection in undirected graph using BFS
```
```
### Topological Sorting using DFS - only in DAGs
```
def dfs(adj, curr_node, vis):
    vis.add(curr_node)
    for next_node in adj[curr_node]:
        if next_node not in vis:
            dfs(adj, next_node, vis)
    stack.add(curr_node)

for curr_node in range(len(nodes)):
    if curr_node not in vis:
        dfs(adj, curr_node, vis)
print(the stack)
```
### Topological Sorting using BFS - only in DAGs, Kahn's Algorithm
```
```
### Disjoint Set - Union Find
```
def find(node, parent):
    if node == parent[node]:
        return node
    
    return find(parent[node], parent)

def union(node_a, node_b, parent):
    par_a = find(node_a, parent)
    par_b = find(node_b, parent)
    if par_a != par_b:
        parent[par_a] = par_b

```
### Disjoint set - Union Find by rank and collapsing find for path compression
```
def find(node, parent):
    if node == parent[node]:
        return node
    
    return parent[node] = find(parent[node], parent)

def union(node_a, node_b, parent, rank):
    par_a = find(node_a, parent)
    par_b = find(node_b, parent)
    if par_a != par_b:
        rank_a = rank[par_a]
        rank_b = rank[par_b]
        if rank_a > rank_b:
            parent[par_b] = par_a
            rank[par_a] += rank[par_b]
        else:
            parent[par_a] = par_b
            rank[par_b] += rank[par_a]
    else:
        return
```
### Disjoint set - Union Find for Cycle detection
```
```
### Dijktra Algorithm
```
```
### Floyed Warshall Algorithm
```
```
### Prims Algorithm for MST
```
```
### Krushkals Algorithm for MST
```
```
### Eular Path
```
```