"""
1269. Number of Ways to Stay in the Same Place After Some Steps (Hard)

Pattern: 19_linear_dp
- Count ways to return to index 0 after exactly `steps` moves (left, right, or stay).

Approach:
- dp[steps][pos] = number of ways to be at position pos after using `steps` moves.
- The maximum reachable position is min(steps // 2, arrLen - 1) since we need to
  return to 0, so we can go at most steps/2 positions right.
- Base: dp[0][0] = 1.
- Transition: dp[s][p] = dp[s-1][p] + dp[s-1][p-1] + dp[s-1][p+1] (stay, came from left, came from right).
- Answer: dp[steps][0].

Complexity:
- Time:  O(steps * min(steps, arrLen))
- Space: O(min(steps, arrLen))
"""

MOD = 10**9 + 7


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_pos = min(steps // 2, arrLen - 1)

        dp = [0] * (max_pos + 1)
        dp[0] = 1

        for s in range(1, steps + 1):
            new_dp = [0] * (max_pos + 1)
            for p in range(max_pos + 1):
                new_dp[p] = dp[p]  # stay
                if p > 0:
                    new_dp[p] = (new_dp[p] + dp[p - 1]) % MOD
                if p < max_pos:
                    new_dp[p] = (new_dp[p] + dp[p + 1]) % MOD
            dp = new_dp

        return dp[0]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: steps=3, arrLen=2 -> 4
    assert sol.numWays(3, 2) == 4

    # Example 2: steps=2, arrLen=4 -> 2
    assert sol.numWays(2, 4) == 2

    # Example 3: steps=4, arrLen=2 -> 8
    assert sol.numWays(4, 2) == 8

    # steps=1: only "stay" works -> 1
    assert sol.numWays(1, 1) == 1

    # Large steps, small array
    assert sol.numWays(27, 7) == 127784505

    print("All tests passed!")


if __name__ == "__main__":
    test()
