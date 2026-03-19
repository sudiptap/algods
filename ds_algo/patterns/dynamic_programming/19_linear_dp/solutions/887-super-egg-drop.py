"""
887. Super Egg Drop (Hard)
https://leetcode.com/problems/super-egg-drop/

Given k eggs and n floors, find the minimum number of moves to determine the
critical floor (highest floor from which an egg can be dropped without breaking).

Pattern: Linear DP
Approach:
- Reframe: dp[m][k] = max number of floors we can check with m moves and k eggs.
- dp[m][k] = dp[m-1][k-1] + dp[m-1][k] + 1
  (egg breaks: check dp[m-1][k-1] floors below;
   egg survives: check dp[m-1][k] floors above; plus current floor)
- Find smallest m such that dp[m][k] >= n.

Time:  O(k * log(n)) — m grows at most O(log n) for fixed k >= 2.
Space: O(k) — only need previous row.
"""


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """Return minimum moves to find critical floor.

        Args:
            k: Number of eggs, 1 <= k <= 100.
            n: Number of floors, 1 <= n <= 10^4.

        Returns:
            Minimum number of moves in worst case.
        """
        # dp[j] = max floors checkable with current number of moves and j eggs
        dp = [0] * (k + 1)
        m = 0
        while dp[k] < n:
            m += 1
            # Update in reverse to avoid overwriting needed values
            for j in range(k, 0, -1):
                dp[j] = dp[j - 1] + dp[j] + 1
        return m


# ---------- tests ----------
def test_super_egg_drop():
    sol = Solution()

    # Example 1: k=1, n=2 -> 2 (must try each floor from bottom)
    assert sol.superEggDrop(1, 2) == 2

    # Example 2: k=2, n=6 -> 3
    assert sol.superEggDrop(2, 6) == 3

    # Example 3: k=3, n=14 -> 4
    assert sol.superEggDrop(3, 14) == 4

    # k=1, n=1 -> 1
    assert sol.superEggDrop(1, 1) == 1

    # k=2, n=1 -> 1
    assert sol.superEggDrop(2, 1) == 1

    # k=1, n=100 -> 100
    assert sol.superEggDrop(1, 100) == 100

    # k=2, n=100 -> 14
    assert sol.superEggDrop(2, 100) == 14

    print("All tests passed for 887. Super Egg Drop")


if __name__ == "__main__":
    test_super_egg_drop()
