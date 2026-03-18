"""
343. Integer Break (Medium)

Given an integer n >= 2, break it into the sum of at least two positive
integers and maximize the product of those integers.

Approach:
    DP: dp[i] = max over j in [1..i-1] of max(j*(i-j), j*dp[i-j])
    - j*(i-j): break into exactly two parts
    - j*dp[i-j]: break i-j further

    Math insight: use as many 3s as possible. If remainder is 1, replace
    one 3 with two 2s (3+1=4 -> 2+2, product 4 > 3).

Time:  O(n^2) for DP, O(1) for math approach
Space: O(n) for DP, O(1) for math approach
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        """Return the maximum product from breaking n into at least 2 parts."""
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


class SolutionMath:
    def integerBreak(self, n: int) -> int:
        """Math approach: maximize product using 3s and 2s."""
        if n == 2:
            return 1
        if n == 3:
            return 2

        product = 1
        while n > 4:
            product *= 3
            n -= 3
        product *= n  # remaining n is 2, 3, or 4
        return product


# ---------- Tests ----------

def test():
    for cls in [Solution, SolutionMath]:
        s = cls()

        assert s.integerBreak(2) == 1   # 1+1
        assert s.integerBreak(3) == 2   # 1+2
        assert s.integerBreak(4) == 4   # 2+2
        assert s.integerBreak(5) == 6   # 2+3
        assert s.integerBreak(6) == 9   # 3+3
        assert s.integerBreak(7) == 12  # 3+4 -> 3+2+2
        assert s.integerBreak(8) == 18  # 3+3+2
        assert s.integerBreak(10) == 36 # 3+3+4 -> 3+3+2+2

    print("All tests passed!")


if __name__ == "__main__":
    test()
