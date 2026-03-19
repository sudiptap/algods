"""
2787. Ways to Express an Integer as Sum of Powers
https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

Pattern: 03 - Unbounded Knapsack (actually 0/1 knapsack with unique bases)

---
APPROACH: Each integer i from 1..n can be used at most once. Compute i^x for
valid i (where i^x <= n). Standard 0/1 knapsack: dp[j] = ways to form sum j.

Time: O(n * n^(1/x))  Space: O(n)
---
"""

MOD = 10**9 + 7


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        i = 1
        while i ** x <= n:
            power = i ** x
            for j in range(n, power - 1, -1):
                dp[j] = (dp[j] + dp[j - power]) % MOD
            i += 1

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfWays(10, 2) == 1   # 1^2 + 3^2 = 10
    assert sol.numberOfWays(4, 1) == 2    # {4}, {1,3}
    assert sol.numberOfWays(1, 1) == 1    # {1}

    print("All tests passed!")
