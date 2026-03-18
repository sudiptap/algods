"""
1799. Maximize Score After N Operations
https://leetcode.com/problems/maximize-score-after-n-operations/

Pattern: 11 - Bitmask DP

---
APPROACH: Bitmask DP with precomputed GCDs
- We have 2n numbers and perform n operations. In operation i (1-indexed),
  pick any two unused numbers, score += i * gcd(nums[a], nums[b]).
- State: bitmask of which numbers are used. The operation number is
  determined by popcount(mask) // 2 + 1.
- dp[mask] = max score achievable from the remaining numbers.
- Precompute gcd(nums[i], nums[j]) for all pairs.
- Enumerate all pairs of unset bits in the complement of mask.

Time: O(2^(2n) * n^2)  Space: O(2^(2n))
  With 2n <= 14, this is feasible: 2^14 = 16384 states.
---
"""

from typing import List
from math import gcd
from functools import lru_cache


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """
        Bitmask DP. mask tracks which elements have been used.
        Operation number = popcount(mask)//2 + 1.
        Try all pairs of unused elements and pick the best.
        """
        m = len(nums)  # m = 2n

        # Precompute GCDs
        g = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                g[i][j] = g[j][i] = gcd(nums[i], nums[j])

        full_mask = (1 << m) - 1

        @lru_cache(maxsize=None)
        def dp(mask: int) -> int:
            if mask == full_mask:
                return 0

            used = bin(mask).count('1')
            op = used // 2 + 1  # current operation number (1-indexed)

            best = 0
            # Find first unused index
            for i in range(m):
                if mask & (1 << i):
                    continue
                for j in range(i + 1, m):
                    if mask & (1 << j):
                        continue
                    new_mask = mask | (1 << i) | (1 << j)
                    score = op * g[i][j] + dp(new_mask)
                    best = max(best, score)
                # Only pair i with elements j > i, then break to avoid
                # redundant orderings: always pick the smallest unused as first
                break

            return best

        return dp(0)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: nums = [1,2], n=1 -> 1*gcd(1,2) = 1
    assert sol.maxScore([1, 2]) == 1

    # Example 2: nums = [3,4,6,8], n=2
    # Op1: gcd(3,6)=3 -> 1*3=3, Op2: gcd(4,8)=4 -> 2*4=8, total=11
    assert sol.maxScore([3, 4, 6, 8]) == 11

    # Example 3: nums = [1,2,3,4,5,6], n=3
    assert sol.maxScore([1, 2, 3, 4, 5, 6]) == 14

    # All same
    assert sol.maxScore([6, 6, 6, 6]) == 18  # 1*6 + 2*6 = 18

    # Two elements with gcd 1
    assert sol.maxScore([7, 11]) == 1

    print("Solution: all tests passed")
