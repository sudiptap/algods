"""
1872. Stone Game VIII (Hard)
https://leetcode.com/problems/stone-game-viii/

Alice and Bob play a game with stones. On each turn, a player picks up
the leftmost x >= 2 stones, removes them, and places a new stone with
their sum. The player scores the sum of the picked stones. Both play
optimally. Return Alice's score minus Bob's score.

Pattern: Interval DP / Prefix Sum DP
Approach:
- Let prefix[i] = sum of stones[0..i].
- When a player picks the first x stones, they score prefix[x].
  The remaining state is equivalent to having prefix[x] as the first stone.
- dp[i] = max difference the current player can achieve when choosing
  from prefix[i..n-1]. The current player picks prefix[i] and opponent
  gets dp[i+1].
- dp[i] = max(prefix[i] - dp[i+1], dp[i+1]) ... but actually:
  dp[i] = max(prefix[i] - dp[i+1], dp[i+1]) is wrong.
- Correct: dp[i] = max over j>=i of (prefix[j] - dp[j+1]).
  Since dp[n-1] = prefix[n-1], work backwards:
  dp[i] = max(prefix[i] - dp[i+1], dp[i+1])
- Answer: dp[1] (must pick at least 2 stones, so start from index 1).

Time:  O(n)
Space: O(n) for prefix sums, O(1) extra for dp
"""

from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        """Return Alice score minus Bob score when both play optimally.

        Args:
            stones: List of stone values.

        Returns:
            Score difference (Alice - Bob).
        """
        n = len(stones)
        # Build prefix sums
        prefix = stones[:]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        # dp from right to left
        # dp[n-1] = prefix[n-1] (must take all remaining)
        dp = prefix[n - 1]
        for i in range(n - 2, 0, -1):
            # Current player can take prefix[i] and get prefix[i] - dp_next
            # or skip (which means dp stays same)
            dp = max(prefix[i] - dp, dp)

        return dp


# ---------- tests ----------
def test_stone_game_viii():
    sol = Solution()

    # Example 1: [-1,2,-3,4,-5] -> 5
    assert sol.stoneGameVIII([-1, 2, -3, 4, -5]) == 5

    # Example 2: [7,-6,5,10,5,-2,-6] -> 13
    assert sol.stoneGameVIII([7, -6, 5, 10, 5, -2, -6]) == 13

    # Example 3: [-10,-12] -> -22
    assert sol.stoneGameVIII([-10, -12]) == -22

    # Two positive stones
    assert sol.stoneGameVIII([1, 2]) == 3

    print("All tests passed for 1872. Stone Game VIII")


if __name__ == "__main__":
    test_stone_game_viii()
