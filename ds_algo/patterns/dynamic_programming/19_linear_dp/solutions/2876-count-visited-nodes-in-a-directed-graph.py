"""
2876. Count Visited Nodes in a Directed Graph
https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

Pattern: 19 - Linear DP (Find cycles in functional graph)

---
APPROACH: Each node has exactly one outgoing edge (functional graph). Find all
cycles. Nodes in a cycle can visit cycle_length nodes. Nodes not in a cycle
(tails) visit their distance to the cycle + cycle_length. Use iterative
cycle detection with coloring.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [0] * n
        # 0 = unvisited, 1 = in progress, 2 = done
        color = [0] * n

        for start in range(n):
            if color[start] == 2:
                continue

            # Trace path from start
            path = []
            node = start
            while color[node] == 0:
                color[node] = 1
                path.append(node)
                node = edges[node]

            if color[node] == 1:
                # Found a cycle: find where cycle starts in path
                cycle_start = path.index(node)
                cycle_len = len(path) - cycle_start

                # Mark cycle nodes
                for i in range(cycle_start, len(path)):
                    ans[path[i]] = cycle_len
                    color[path[i]] = 2

                # Mark tail nodes (before cycle)
                for i in range(cycle_start - 1, -1, -1):
                    ans[path[i]] = ans[path[i + 1]] + 1
                    color[path[i]] = 2
            else:
                # node is already done, chain from it
                for i in range(len(path) - 1, -1, -1):
                    ans[path[i]] = ans[node] + (len(path) - i)
                    color[path[i]] = 2

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countVisitedNodes([1, 2, 0, 0]) == [3, 3, 3, 4]
    assert sol.countVisitedNodes([1, 2, 3, 4, 0]) == [5, 5, 5, 5, 5]

    print("All tests passed!")
