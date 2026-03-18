"""
375. Guess Number Higher or Lower II (Medium)

We pick a number from 1 to n. Each wrong guess k costs k dollars.
Find the minimum amount of money needed to guarantee a win regardless
of which number was picked.

Pattern: Matrix Chain Multiplication / Interval DP.

Approach:
    dp[i][j] = minimum cost to guarantee finding the answer in range [i, j].
    For each candidate guess k in [i, j]:
        cost = k + max(dp[i][k-1], dp[k+1][j])
    We take the max of left/right because the adversary picks the worst case,
    then we minimize over all choices of k.

    Base cases:
        - dp[i][i] = 0  (only one number, no guess needed)
        - dp[i][j] = 0 when i > j (empty range)

    Fill bottom-up by increasing interval length.

Time:  O(n^3)
Space: O(n^2)
"""


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """Return the minimum cost to guarantee winning the guessing game [1..n]."""
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for length in range(2, n + 1):            # interval length
            for i in range(1, n - length + 2):     # start
                j = i + length - 1                  # end
                dp[i][j] = float('inf')
                for k in range(i, j + 1):           # guess
                    cost = k + max(dp[i][k - 1], dp[k + 1][j])
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][n]


# ───────────────────────── Tests ─────────────────────────
def test():
    s = Solution()

    # n=1: only one number, cost 0
    assert s.getMoneyAmount(1) == 0

    # n=2: guess 1 (cost 1); if wrong, it's 2. Total = 1
    assert s.getMoneyAmount(2) == 1

    # n=3: guess 2 (cost 2); left=1 right=3, both determined. Total = 2
    assert s.getMoneyAmount(3) == 2

    # n=10: known answer = 16
    assert s.getMoneyAmount(10) == 16, f"Got {s.getMoneyAmount(10)}"

    # n=5: known answer = 6
    assert s.getMoneyAmount(5) == 6, f"Got {s.getMoneyAmount(5)}"

    print("All tests passed for 375!")


if __name__ == "__main__":
    test()
