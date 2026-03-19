"""
1259. Handshakes That Don't Cross (Hard)

Pattern: 15_counting_combinatorial
- Count ways for 2n people in a circle to shake hands pairwise without crossings.

Approach:
- This is the Catalan number C(n).
- dp[0] = 1 (base case, 0 people).
- dp[n] = sum(dp[i] * dp[n-1-i]) for i in [0, n-1].
  Intuition: fix person 0. They shake hands with person 2k+1 (must be odd-indexed
  to have even number of people on each side). This splits into two independent
  sub-problems of sizes 2k and 2(n-1-k).
- The number of people is numPeople = 2n, so we compute dp[numPeople // 2].

Complexity:
- Time:  O(n^2) where n = numPeople / 2
- Space: O(n)
"""

MOD = 10**9 + 7


class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        n = numPeople // 2
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % MOD

        return dp[n]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: 2 people -> 1 way
    assert sol.numberOfWays(2) == 1

    # Example 2: 4 people -> 2 ways
    assert sol.numberOfWays(4) == 2

    # Example 3: 6 people -> 5 ways (Catalan(3) = 5)
    assert sol.numberOfWays(6) == 5

    # Example 4: 8 people -> 14 ways (Catalan(4) = 14)
    assert sol.numberOfWays(8) == 14

    # Larger: 10 people -> Catalan(5) = 42
    assert sol.numberOfWays(10) == 42

    print("All tests passed!")


if __name__ == "__main__":
    test()
