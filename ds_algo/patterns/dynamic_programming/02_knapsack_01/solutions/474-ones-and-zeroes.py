"""
474. Ones and Zeroes (Medium)

Pattern: 02_knapsack_01 (2D 0/1 Knapsack)
- dp[i][j] = maximum number of strings that can be formed using at most i zeros and j ones.

Approach:
- Count zeros and ones for each string.
- Use a 2D DP table of size (m+1) x (n+1).
- For each string, iterate the DP table in reverse (right-to-left, bottom-to-top)
  to ensure each string is used at most once (standard 0/1 knapsack trick).
- Transition: dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

Complexity:
- Time:  O(L * m * n) where L = number of strings
- Space: O(m * n) for the DP table
"""

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            # Iterate in reverse to avoid using the same string twice
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4

    # Example 2
    assert sol.findMaxForm(["10", "0", "1"], 1, 1) == 2

    # No strings
    assert sol.findMaxForm([], 5, 5) == 0

    # Zero budget
    assert sol.findMaxForm(["10", "01"], 0, 0) == 0

    # Single string fits
    assert sol.findMaxForm(["0"], 1, 0) == 1

    # Single string doesn't fit
    assert sol.findMaxForm(["11"], 1, 0) == 0

    # All same strings
    assert sol.findMaxForm(["01", "01", "01"], 3, 3) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
