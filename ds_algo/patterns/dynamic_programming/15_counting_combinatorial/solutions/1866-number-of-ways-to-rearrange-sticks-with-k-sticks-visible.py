"""
1866. Number of Ways to Rearrange Sticks With K Sticks Visible (Hard)
https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

There are n uniquely-sized sticks. Arrange them in a row so that exactly
k sticks are visible from the left (a stick is visible if no taller
stick is to its left). Return the number of such arrangements mod 10^9+7.

Pattern: Counting / Combinatorial (Stirling Numbers of the First Kind)
Approach:
- dp[n][k] = number of permutations of n elements with exactly k
  left-to-right maxima (records).
- Recurrence: dp[n][k] = dp[n-1][k-1] + (n-1) * dp[n-1][k]
  - The tallest stick (n) is placed last (leftmost visible): dp[n-1][k-1]
  - Any of the other (n-1) sticks is placed last (not visible): (n-1)*dp[n-1][k]
- This is the unsigned Stirling number of the first kind.
- Base: dp[0][0] = 1.

Time:  O(n * k)
Space: O(n * k), reducible to O(k) with rolling array
"""


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """Return number of permutations of n sticks with k visible from left.

        Args:
            n: Number of sticks.
            k: Required number of visible sticks.

        Returns:
            Count of valid arrangements mod 10^9 + 7.
        """
        MOD = 10**9 + 7
        # dp[j] = ways for current n' with j visible
        dp = [0] * (k + 1)
        dp[0] = 1  # dp[0][0] = 1

        for i in range(1, n + 1):
            new_dp = [0] * (k + 1)
            for j in range(1, k + 1):
                new_dp[j] = (dp[j - 1] + (i - 1) * dp[j]) % MOD
            dp = new_dp

        return dp[k]


# ---------- tests ----------
def test_rearrange_sticks():
    sol = Solution()

    # Example 1: n=3, k=2 -> 3
    assert sol.rearrangeSticks(3, 2) == 3

    # Example 2: n=5, k=5 -> 1 (only sorted order)
    assert sol.rearrangeSticks(5, 5) == 1

    # Example 3: n=20, k=11 -> 647427950
    assert sol.rearrangeSticks(20, 11) == 647427950

    # n=1, k=1 -> 1
    assert sol.rearrangeSticks(1, 1) == 1

    # n=3, k=1 -> 2 (tallest must be first, 2 arrangements of rest)
    assert sol.rearrangeSticks(3, 1) == 2

    print("All tests passed for 1866. Number of Ways to Rearrange Sticks")


if __name__ == "__main__":
    test_rearrange_sticks()
