"""
2741. Special Permutations
https://leetcode.com/problems/special-permutations/

Pattern: 11 - Bitmask DP (dp[mask][last])

---
APPROACH: dp[mask][last] = number of permutations using elements in mask
where the last element placed is nums[last]. Transition: try adding each
unused element that divides or is divisible by the current last.

Time: O(2^n * n^2)  Space: O(2^n * n)
---
"""

from typing import List
from functools import lru_cache

MOD = 10**9 + 7


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(mask, last):
            if mask == (1 << n) - 1:
                return 1
            res = 0
            for i in range(n):
                if mask & (1 << i):
                    continue
                if nums[last] % nums[i] == 0 or nums[i] % nums[last] == 0:
                    res = (res + dp(mask | (1 << i), i)) % MOD
            return res

        ans = 0
        for i in range(n):
            ans = (ans + dp(1 << i, i)) % MOD
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.specialPerm([2, 3, 6]) == 2
    assert sol.specialPerm([1, 4, 3]) == 2

    print("All tests passed!")
