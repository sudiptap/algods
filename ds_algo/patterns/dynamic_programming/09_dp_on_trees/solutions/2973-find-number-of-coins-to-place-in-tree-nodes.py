"""
2973. Find Number of Coins to Place in Tree Nodes

Pattern: DP on Trees
Approach: Post-order DFS. For each node, track the 3 largest and 2 smallest costs
    in its subtree (to maximize product of 3 values, consider 3 largest or 1 largest + 2 smallest).
    If subtree has < 3 nodes, place 1 coin; otherwise place max(0, max_product).
Time Complexity: O(n log n) due to sorting small lists
Space Complexity: O(n)
"""
from collections import defaultdict

def placedCoins(edges, cost):
    n = len(cost)
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    result = [0] * n

    def dfs(node, parent):
        # Returns sorted list of up to 5 values (3 largest + 2 smallest) from subtree
        vals = [cost[node]]
        for child in adj[node]:
            if child != parent:
                child_vals = dfs(child, node)
                vals.extend(child_vals)

        vals.sort()
        # Keep only relevant values: 2 smallest + 3 largest (at most 5)
        if len(vals) > 5:
            vals = vals[:2] + vals[-3:]

        if len(vals) < 3:
            result[node] = 1
        else:
            # Max product of any 3: either 3 largest or 2 smallest * 1 largest
            candidates = [vals[-1] * vals[-2] * vals[-3],
                         vals[0] * vals[1] * vals[-1]]
            result[node] = max(0, max(candidates))

        return vals

    dfs(0, -1)
    return result


def test():
    r = placedCoins([[0,1],[0,2],[0,3],[0,4],[0,5]], [1,2,3,4,5,6])
    assert r[0] == 120  # 4*5*6
    r2 = placedCoins([[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]],
                     [1,4,2,3,5,7,8,-4,2])
    assert r2[0] == 280  # 5*7*8
    # subtree of node 2: nodes [2,6,7,8], costs [2,8,-4,2], best=max(0, 2*8*2, (-4)*2*8)=32
    assert r2[2] == 32
    print("All tests passed!")

test()
