"""
1692. Count Ways to Distribute Candies
https://leetcode.com/problems/count-ways-to-distribute-candies/

Pattern: 15 - Counting / Combinatorial DP

---
APPROACH: Stirling numbers of the second kind
- Distribute n unique candies into k non-empty, indistinguishable bags.
- This is exactly S(n, k) - Stirling number of the second kind.
- Recurrence: S(n, k) = k * S(n-1, k) + S(n-1, k-1)
  - Either place candy n into one of k existing bags: k * S(n-1, k)
  - Or create a new bag with candy n alone: S(n-1, k-1)
- Base: S(0, 0) = 1, S(n, 0) = 0 for n > 0, S(0, k) = 0 for k > 0.

Time: O(n * k)
Space: O(n * k), can be O(k) with rolling array
---
"""

MOD = 10**9 + 7


class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        # dp[i][j] = S(i, j) = ways to distribute i candies into j non-empty bags
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                dp[i][j] = (j * dp[i - 1][j] + dp[i - 1][j - 1]) % MOD

        return dp[n][k]


# --- Tests ---
def test():
    sol = Solution()

    assert sol.waysToDistribute(3, 2) == 3  # S(3,2) = 3
    assert sol.waysToDistribute(4, 2) == 7  # S(4,2) = 7
    assert sol.waysToDistribute(20, 5) == 206085257
    assert sol.waysToDistribute(1, 1) == 1
    assert sol.waysToDistribute(5, 5) == 1
    assert sol.waysToDistribute(5, 1) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
