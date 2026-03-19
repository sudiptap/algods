"""
837. New 21 Game
https://leetcode.com/problems/new-21-game/

Pattern: 17 - Probability DP

---
APPROACH: DP with sliding window sum
- dp[i] = probability of reaching score exactly i.
- dp[0] = 1. For i >= 1: dp[i] = sum(dp[i-maxPts..i-1]) / maxPts
  (but only from valid previous scores < k).
- Use a sliding window sum to compute the running sum efficiently.
- Answer = sum(dp[k..n]).

Time: O(n + maxPts)  Space: O(n)
---
"""


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0  # sum of dp values in the sliding window

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts

            if i < k:
                window_sum += dp[i]  # add to window (can still draw from here)
            if i >= maxPts:
                window_sum -= dp[i - maxPts]  # slide window

        return sum(dp[k:n + 1])


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert abs(sol.new21Game(10, 1, 10) - 1.0) < 1e-5
    assert abs(sol.new21Game(6, 1, 10) - 0.6) < 1e-5
    assert abs(sol.new21Game(21, 17, 10) - 0.73278) < 1e-4
    assert sol.new21Game(0, 0, 1) == 1.0

    print("all tests passed")
