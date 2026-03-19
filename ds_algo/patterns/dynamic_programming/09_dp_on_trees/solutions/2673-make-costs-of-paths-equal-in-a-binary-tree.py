"""
2673. Make Costs of Paths Equal in a Binary Tree
https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

Pattern: 09 - DP on Trees (Greedy bottom-up)

---
APPROACH: Process nodes bottom-up. For each internal node, make its two
children's subtree sums equal by incrementing the smaller one. The total
increments needed is sum of |left_sum - right_sum| across all internal nodes.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        # Process from last internal node to root (0-indexed: nodes n//2-1 down to 0)
        # Children of node i (0-indexed) are 2i+1 and 2i+2
        for i in range(n // 2 - 1, -1, -1):
            left = 2 * i + 1
            right = 2 * i + 2
            ans += abs(cost[left] - cost[right])
            # Propagate max child cost up
            cost[i] += max(cost[left], cost[right])
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minIncrements(7, [1, 5, 2, 2, 3, 3, 1]) == 6
    assert sol.minIncrements(3, [5, 3, 3]) == 0

    print("All tests passed!")
