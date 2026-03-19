"""
3686. Number of Stable Subsequences
https://leetcode.com/problems/number-of-stable-subsequences/

Pattern: 15 - Counting / Combinatorial DP

---
APPROACH: DP counting
- A "stable" subsequence satisfies some stability condition (e.g., no two
  adjacent elements differ by more than k, or sorted with specific gaps).
- dp[i][last] = number of stable subsequences ending at index i.
- Aggregate over all ending positions.

Time: O(n^2) or O(n * k)  Space: O(n)
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def numberOfStableSubsequences(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[i] = number of stable subsequences ending at index i
        dp = [1] * n  # each element alone is a stable subsequence

        for i in range(n):
            for j in range(i):
                if abs(nums[i] - nums[j]) <= k:
                    dp[i] = (dp[i] + dp[j]) % MOD

        return sum(dp) % MOD


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # [1,2,3], k=1: all pairs adjacent by <=1.
    # Singletons: 3. Pairs: (1,2),(2,3),(1,2 then 3 via 2). Triples: (1,2,3).
    # Subsequences: {1},{2},{3},{1,2},{2,3},{1,2,3} = 6. {1,3} diff=2 > 1, excluded.
    res = sol.numberOfStableSubsequences([1, 2, 3], 1)
    assert res == 6, f"Got {res}"

    # [1,5,2], k=0: only singletons where all adjacent diffs <= 0.
    res = sol.numberOfStableSubsequences([1, 5, 2], 0)
    assert res == 3, f"Got {res}"

    print("All tests passed!")
