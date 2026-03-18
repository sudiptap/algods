"""
2466. Count Ways To Build Good Strings
https://leetcode.com/problems/count-ways-to-build-good-strings/

Pattern: 01 - Fibonacci Pattern

---
APPROACH:
dp[i] = number of ways to build a string of length i.
Transitions: dp[i] += dp[i - zero] + dp[i - one]
(append '0' zero times or '1' one times).
Base: dp[0] = 1 (empty string).
Answer: sum(dp[low..high]) mod 10^9+7.

Time: O(high)  Space: O(high)
---
"""

MOD = 10**9 + 7


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """Return the number of good strings with length in [low, high] mod 10^9+7."""
        dp = [0] * (high + 1)
        dp[0] = 1
        ans = 0

        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD
            if i >= low:
                ans = (ans + dp[i]) % MOD

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: low=3, high=3, zero=1, one=1 -> 8
    assert sol.countGoodStrings(3, 3, 1, 1) == 8
    # Example 2: low=2, high=3, zero=1, one=2 -> 5
    assert sol.countGoodStrings(2, 3, 1, 2) == 5
    # Minimum case
    assert sol.countGoodStrings(1, 1, 1, 1) == 2  # "0" or "1"
    # Large range should work without error
    result = sol.countGoodStrings(1, 100000, 1, 1)
    assert 0 < result < MOD

    print("all tests passed")
