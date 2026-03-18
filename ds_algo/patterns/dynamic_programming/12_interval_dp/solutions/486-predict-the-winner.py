"""
486. Predict the Winner (Medium)
https://leetcode.com/problems/predict-the-winner/

Pattern: Interval DP

Given an integer array nums, two players take turns picking from either end.
Player 1 starts. Return True if Player 1 can win (or tie).

Approach:
    dp[i][j] = maximum score difference the current player can achieve
    from nums[i..j].  On their turn the current player picks left or right
    and the subproblem flips sign (opponent becomes current player).

    dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])

    Base case: dp[i][i] = nums[i]  (only one element to pick).
    Answer: dp[0][n-1] >= 0.

Time:  O(n^2)
Space: O(n^2)  — can be reduced to O(n) with 1-D rolling.
"""

from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        """Return True if Player 1 can win or tie."""
        n = len(nums)
        # dp[i][j] = best score diff current player achieves on nums[i..j]
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                    nums[i] - dp[i + 1][j],
                    nums[j] - dp[i][j - 1],
                )

        return dp[0][n - 1] >= 0


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().predictTheWinner([1, 5, 2]) is False

def test_example2():
    assert Solution().predictTheWinner([1, 5, 233, 7]) is True

def test_single():
    assert Solution().predictTheWinner([5]) is True

def test_two_elements():
    assert Solution().predictTheWinner([1, 2]) is True

def test_tie():
    # [1, 1] -> Player 1 picks 1, Player 2 picks 1, tie -> Player 1 wins
    assert Solution().predictTheWinner([1, 1]) is True

def test_symmetric():
    assert Solution().predictTheWinner([1, 2, 3, 4]) is True

def test_all_same():
    assert Solution().predictTheWinner([7, 7, 7, 7]) is True


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
