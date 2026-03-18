"""
312. Burst Balloons (Hard)
https://leetcode.com/problems/burst-balloons/

You are given n balloons, indexed from 0 to n-1. Each balloon is painted with
a number on it represented by array nums. You are asked to burst all the
balloons. If you burst balloon i you will get nums[i-1] * nums[i] * nums[i+1]
coins. If i-1 or i+1 goes out of bounds, treat it as if there is a balloon
with a 1 painted on it.

Return the maximum coins you can collect by bursting all the balloons wisely.

Pattern: Matrix Chain Multiplication / Interval DP
- Pad nums with 1 on both ends: arr = [1] + nums + [1].
- dp[i][j] = max coins from bursting all balloons between i and j (exclusive).
- For each k in (i+1 .. j-1), treat k as the *last* balloon burst in the
  interval. Coins from k = arr[i] * arr[k] * arr[j] + dp[i][k] + dp[k][j].
- Build bottom-up by increasing interval length.

Time:  O(n^3)
Space: O(n^2)
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """Return the maximum coins from bursting all balloons.

        Args:
            nums: List of balloon values, 1 <= len(nums) <= 300.

        Returns:
            Maximum coins obtainable.
        """
        arr = [1] + nums + [1]
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        # length is the gap between i and j (exclusive endpoints)
        for length in range(2, n):           # min gap of 2 to have at least one balloon
            for i in range(0, n - length):
                j = i + length
                for k in range(i + 1, j):    # k is the last balloon burst
                    coins = arr[i] * arr[k] * arr[j] + dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], coins)

        return dp[0][n - 1]


# ---------- tests ----------
def test_burst_balloons():
    sol = Solution()

    # Example 1: [3,1,5,8] -> best order gives 167
    assert sol.maxCoins([3, 1, 5, 8]) == 167, f"Expected 167, got {sol.maxCoins([3, 1, 5, 8])}"

    # Example 2: single balloon
    assert sol.maxCoins([1]) == 1

    # Two balloons [1,5]: burst 1 first -> 1*1*5 + 1*5*1 = 10
    assert sol.maxCoins([1, 5]) == 10

    # All ones [1,1,1] -> 3
    assert sol.maxCoins([1, 1, 1]) == 3

    # Edge: large single balloon
    assert sol.maxCoins([100]) == 100

    print("All tests passed for 312. Burst Balloons")


if __name__ == "__main__":
    test_burst_balloons()
