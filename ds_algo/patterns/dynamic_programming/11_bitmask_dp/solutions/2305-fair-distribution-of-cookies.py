"""
2305. Fair Distribution of Cookies
https://leetcode.com/problems/fair-distribution-of-cookies/

Pattern: 11 - Bitmask DP

---
APPROACH: Backtracking with pruning / Bitmask DP
- dp[mask] = min total cookies for subset mask (precompute).
- Then distribute: dp2[j][mask] = min unfairness distributing cookies in mask to j children.
- Enumerate submasks for each child.
- Alternatively, backtracking: assign each bag to one of k children, prune when
  current max exceeds best answer.

Time: O(k * 3^n) for subset enumeration  Space: O(k * 2^n)
---
"""

from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        # Precompute sum for each subset
        subset_sum = [0] * (1 << n)
        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i):
                    subset_sum[mask] += cookies[i]

        # dp[j][mask] = min of max cookies when distributing mask among j people
        # Optimize: use 1D dp over k iterations
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        # For k=1, dp[mask] = subset_sum[mask]
        prev = list(subset_sum)

        for child in range(1, k):
            cur = [float('inf')] * (1 << n)
            for mask in range(1 << n):
                # Enumerate submasks of mask for this child
                sub = mask
                while sub > 0:
                    rest = mask ^ sub
                    cur[mask] = min(cur[mask], max(subset_sum[sub], prev[rest]))
                    sub = (sub - 1) & mask
            prev = cur

        full = (1 << n) - 1
        return prev[full]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.distributeCookies([8, 15, 10, 20, 8], 2) == 31
    assert sol.distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3) == 7
    assert sol.distributeCookies([1], 1) == 1
    assert sol.distributeCookies([1, 2, 3], 3) == 3

    print("all tests passed")
