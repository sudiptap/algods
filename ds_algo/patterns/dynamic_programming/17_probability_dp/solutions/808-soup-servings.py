"""
808. Soup Servings
https://leetcode.com/problems/soup-servings/

Pattern: 17 - Probability DP

---
APPROACH: Memoized recursion on remaining soup amounts
- Four operations reduce (A, B) by (100,0), (75,25), (50,50), (25,75).
- Each with probability 0.25.
- P(A empties first) + 0.5 * P(both empty simultaneously).
- Normalize by dividing amounts by 25 (ceiling).
- Key insight: for large n (>4800), answer is very close to 1.0
  (within 1e-5), so return 1.0 directly.

Time: O((n/25)^2) capped at ~4800  Space: O((n/25)^2)
---
"""

from functools import lru_cache


class Solution:
    def soupServings(self, n: int) -> float:
        # For large n, probability approaches 1.0
        if n > 4800:
            return 1.0

        # Normalize: divide by 25, ceiling
        m = (n + 24) // 25

        @lru_cache(maxsize=None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5  # both empty
            if a <= 0:
                return 1.0  # A empty first
            if b <= 0:
                return 0.0  # B empty first

            return 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )

        return dp(m, m)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert abs(sol.soupServings(50) - 0.625) < 1e-6
    assert abs(sol.soupServings(100) - 0.71875) < 1e-6
    assert sol.soupServings(0) == 0.5
    assert sol.soupServings(10000) == 1.0  # large n optimization

    print("all tests passed")
