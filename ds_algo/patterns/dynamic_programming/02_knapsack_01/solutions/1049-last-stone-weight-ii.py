"""
1049. Last Stone Weight II
https://leetcode.com/problems/last-stone-weight-ii/

Pattern: 02 - 0/1 Knapsack

---
APPROACH: 0/1 Knapsack (partition into two groups)
- Smashing stones is equivalent to partitioning them into two groups
  and minimizing |sum1 - sum2|.
- This reduces to: find the largest subset sum <= total_sum // 2.
- Use a boolean DP set or bitset to track achievable sums.
- Answer = total_sum - 2 * best_sum_near_half.

Time:  O(n * S)  where S = sum(stones)
Space: O(S)
---
"""

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """Return smallest possible weight of the last remaining stone (or 0)."""
        total = sum(stones)
        half = total // 2

        # dp[j] = True if sum j is achievable using some subset
        dp = [False] * (half + 1)
        dp[0] = True

        for stone in stones:
            # Traverse backwards to avoid using same stone twice
            for j in range(half, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]

        # Find largest achievable sum <= half
        for j in range(half, -1, -1):
            if dp[j]:
                return total - 2 * j

        return total  # should never reach here


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1
    assert sol.lastStoneWeightII([31, 26, 33, 21, 40]) == 5
    assert sol.lastStoneWeightII([1, 2]) == 1
    assert sol.lastStoneWeightII([1]) == 1
    assert sol.lastStoneWeightII([1, 1, 1, 1]) == 0

    print("Solution: all tests passed")
