"""
1406. Stone Game III (Hard)
https://leetcode.com/problems/stone-game-iii/

Pattern: Interval DP / Game Theory

Alice and Bob take turns picking 1, 2, or 3 piles from the front of the
remaining stones. Alice goes first. Both play optimally. Return "Alice",
"Bob", or "Tie" based on who ends up with more stones.

Approach:
    dp[i] = maximum score difference (current player minus opponent) the
    current player can achieve starting from index i.

    dp[i] = max over k in {1,2,3} of (sum(stoneValue[i..i+k-1]) - dp[i+k])

    We iterate i from n-1 down to 0. If dp[0] > 0 Alice wins, dp[0] < 0
    Bob wins, dp[0] == 0 is a tie.

Time:  O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """Return 'Alice', 'Bob', or 'Tie'."""
        n = len(stoneValue)
        # dp[i] = best score diff for current player from index i onward
        # dp[n] = 0 (no stones left)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            total = 0
            for k in range(1, 4):
                if i + k - 1 >= n:
                    break
                total += stoneValue[i + k - 1]
                dp[i] = max(dp[i], total - dp[i + k])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().stoneGameIII([1, 2, 3, 7]) == "Bob"

def test_example2():
    assert Solution().stoneGameIII([1, 2, 3, -9]) == "Alice"

def test_example3():
    assert Solution().stoneGameIII([1, 2, 3, 6]) == "Tie"

def test_single():
    assert Solution().stoneGameIII([5]) == "Alice"

def test_single_negative():
    assert Solution().stoneGameIII([-1]) == "Bob"

def test_two_elements():
    assert Solution().stoneGameIII([1, 1]) == "Alice"

def test_all_negative():
    assert Solution().stoneGameIII([-1, -2, -3]) == "Tie"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
