"""
3241. Time Taken to Mark All Nodes

Pattern: DP on Trees (Rerooting)
Approach: Two-pass rerooting DP. First pass: compute time to mark all nodes in
    subtree rooted at 0 (down DP). Second pass: compute time considering parent's
    subtree (up DP). Time to mark node i's neighbor: 2 if neighbor index is even,
    1 if odd. dp_down[v] = max time to mark all nodes in subtree of v.
Time Complexity: O(n)
Space Complexity: O(n)
"""
from collections import defaultdict

def timeTaken(edges):
    n = len(edges) + 1
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    down = [0] * n  # max time to mark subtree of v (rooted at 0)

    def weight(node):
        """Time to mark node (even=2, odd=1)"""
        return 2 if node % 2 == 0 else 1

    # Pass 1: compute down[v] - DFS from root 0
    order = []
    parent = [-1] * n
    visited = [False] * n
    stack = [0]
    visited[0] = True
    while stack:
        v = stack.pop()
        order.append(v)
        for u in adj[v]:
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                stack.append(u)

    # Process in reverse order (leaves first)
    for v in reversed(order):
        for u in adj[v]:
            if parent[u] == v:  # u is child of v
                down[v] = max(down[v], weight(u) + down[u])

    # Pass 2: compute up[v] - contribution from parent's side
    up = [0] * n  # max time going up from v through parent

    # For rerooting, we need top-2 children contributions for each node
    # to efficiently compute what happens when we remove one child
    top1 = [0] * n  # best child contribution
    top1_child = [-1] * n
    top2 = [0] * n  # second best

    for v in order:
        best1 = best2 = 0
        best1_c = -1
        for u in adj[v]:
            if parent[u] == v:
                val = weight(u) + down[u]
                if val >= best1:
                    best2 = best1
                    best1 = val
                    best1_c = u
                elif val > best2:
                    best2 = val
        top1[v] = best1
        top1_child[v] = best1_c
        top2[v] = best2

    # BFS order to compute up
    for v in order:
        for u in adj[v]:
            if parent[u] == v:  # u is child of v
                # up[u] = weight(v) + max(up[v], best_down_of_v_excluding_u)
                if top1_child[v] == u:
                    best_down_excl = top2[v]
                else:
                    best_down_excl = top1[v]
                up[u] = weight(v) + max(up[v], best_down_excl)

    result = [max(down[v], up[v]) for v in range(n)]
    return result


def test():
    r = timeTaken([[0,1],[0,2]])
    # Node 0(even->w=2): from 0, mark 1(odd->w=1)@t=1, mark 2(even->w=2)@t=2 => max=2
    # Node 1(odd->w=1): from 1, mark 0(even->w=2)@t=2, from 0 mark 2(even->w=2)@t=4 => max=4
    # Node 2(even->w=2): from 2, mark 0(even->w=2)@t=2, from 0 mark 1(odd->w=1)@t=3 => max=3
    assert r == [2, 4, 3], f"Got {r}"
    print("All tests passed!")

test()
