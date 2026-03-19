"""
3004. Maximum Subtree of the Same Color

Pattern: DP on Trees
Approach: Post-order DFS. For each node, check if all nodes in its subtree have
    the same color. Track subtree size and whether subtree is uniform.
Time Complexity: O(n)
Space Complexity: O(n)
"""
from collections import defaultdict

def maximumSubtreeSize(edges, colors):
    n = len(colors)
    if n == 1:
        return 1
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    ans = 0

    def dfs(node, parent):
        nonlocal ans
        size = 1
        uniform = True
        for child in adj[node]:
            if child != parent:
                child_size, child_uniform = dfs(child, node)
                size += child_size
                if not child_uniform or colors[child] != colors[node]:
                    uniform = False
        if uniform:
            ans = max(ans, size)
        return size, uniform

    dfs(0, -1)
    return ans


def test():
    assert maximumSubtreeSize([[0,1],[0,2],[0,3]], [1,1,1,1]) == 4
    assert maximumSubtreeSize([[0,1],[0,2],[0,3]], [1,1,2,3]) == 1
    assert maximumSubtreeSize([[0,1],[0,2],[2,3],[2,4]], [1,2,1,1,1]) == 3
    print("All tests passed!")

test()
