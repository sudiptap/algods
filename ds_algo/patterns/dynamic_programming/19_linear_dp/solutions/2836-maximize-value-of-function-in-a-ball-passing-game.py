"""
2836. Maximize Value of Function in a Ball Passing Game
https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

Pattern: 19 - Linear DP (Binary lifting on functional graph)

---
APPROACH: Binary lifting: precompute for each node, the node reached after
2^j steps and the sum of IDs along the way. Then for a given k, decompose
k in binary and combine jumps. Answer = max over all starting nodes.

Time: O(n log k)  Space: O(n log k)
---
"""

from typing import List


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        LOG = k.bit_length()

        # up[j][i] = node reached from i after 2^j steps
        # cost[j][i] = sum of node IDs from i over 2^j steps (including start, excluding end)
        up = [[0] * n for _ in range(LOG)]
        cost = [[0] * n for _ in range(LOG)]

        for i in range(n):
            up[0][i] = receiver[i]
            cost[0][i] = i  # visiting node i itself

        for j in range(1, LOG):
            for i in range(n):
                mid = up[j - 1][i]
                up[j][i] = up[j - 1][mid]
                cost[j][i] = cost[j - 1][i] + cost[j - 1][mid]

        ans = 0
        for i in range(n):
            cur = i
            total = 0
            for j in range(LOG):
                if k & (1 << j):
                    total += cost[j][cur]
                    cur = up[j][cur]
            total += cur  # add the final landing node
            ans = max(ans, total)

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.getMaxFunctionValue([2, 0, 1], 4) == 6
    assert sol.getMaxFunctionValue([1, 1, 1, 2, 3], 3) == 10

    print("All tests passed!")
