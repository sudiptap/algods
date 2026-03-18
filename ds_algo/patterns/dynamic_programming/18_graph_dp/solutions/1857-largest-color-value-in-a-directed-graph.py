"""
1857. Largest Color Value in a Directed Graph
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

Pattern: 18 - Graph DP (Topological Sort + DP on DAG)

---
APPROACH: Topological sort (Kahn's BFS) + DP
- dp[node][c] = max count of color c on any path ending at node.
- Initialize dp[node][colors[node]] = 1 for every node.
- Process in topological order. When relaxing edge u -> v:
      dp[v][c] = max(dp[v][c], dp[u][c])
  then ensure dp[v][colors[v]] accounts for v's own color.
- If not all nodes are processed, graph has a cycle -> return -1.
- Answer = max over all dp[node][c].

Time:  O((V + E) * 26)   — 26 lowercase letters
Space: O(V * 26)
---
"""

from typing import List
from collections import deque


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """Return the largest color value among all paths, or -1 if a cycle exists."""
        n = len(colors)
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        # dp[node][c] = max count of color c on any path ending at node
        dp = [[0] * 26 for _ in range(n)]

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
            dp[i][ord(colors[i]) - ord('a')] = 1

        processed = 0
        ans = 0

        while queue:
            u = queue.popleft()
            processed += 1
            ans = max(ans, max(dp[u]))

            for v in adj[u]:
                for c in range(26):
                    # propagate color counts from u to v
                    val = dp[u][c] + (1 if c == ord(colors[v]) - ord('a') else 0)
                    dp[v][c] = max(dp[v][c], val)

                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return ans if processed == n else -1


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: cycle
    assert sol.largestPathValue("abaca", [[0,1],[0,2],[2,3],[3,4]]) == 3
    # Example 2: self-loop -> cycle
    assert sol.largestPathValue("a", [[0,0]]) == -1
    # Single node, no edges
    assert sol.largestPathValue("z", []) == 1
    # Linear chain, all same color
    assert sol.largestPathValue("aaaa", [[0,1],[1,2],[2,3]]) == 4
    # Linear chain, all different
    assert sol.largestPathValue("abcd", [[0,1],[1,2],[2,3]]) == 1
    # Diamond: 0->1, 0->2, 1->3, 2->3, colors "aaba"
    assert sol.largestPathValue("aaba", [[0,1],[0,2],[1,3],[2,3]]) == 3

    print("all tests passed")
