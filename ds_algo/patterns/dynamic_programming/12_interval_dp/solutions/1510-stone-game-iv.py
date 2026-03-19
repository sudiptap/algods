"""
1510. Stone Game IV (Hard)
https://leetcode.com/problems/stone-game-iv/

Problem:
    Alice and Bob take turns. On each turn, a player removes a positive
    perfect square number of stones. The player who cannot move loses.
    Alice goes first. Return True if Alice wins with optimal play.

Pattern: 12 - Interval DP (Game Theory)

Approach:
    1. dp[i] = True if the current player wins with i stones remaining.
    2. dp[0] = False (current player loses, no moves).
    3. dp[i] = True if there exists any perfect square k^2 <= i such that
       dp[i - k^2] is False (opponent loses after our move).
    4. Try all perfect squares up to i.

Complexity:
    Time:  O(n * sqrt(n))
    Space: O(n)
"""


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k += 1

        return dp[n]


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1: n=1, Alice takes 1 -> wins
    assert sol.winnerSquareGame(1) is True, "Test 1 failed"

    # Test 2: n=2, Alice takes 1 -> Bob takes 1 -> Alice loses. So Alice wins? No.
    # Alice takes 1, left=1, Bob takes 1, left=0, Alice can't move -> Bob wins. So False.
    assert sol.winnerSquareGame(2) is False, "Test 2 failed"

    # Test 3: n=4, Alice takes 4 -> wins
    assert sol.winnerSquareGame(4) is True, "Test 3 failed"

    # Test 4: n=7
    assert sol.winnerSquareGame(7) is False, f"Test 4 failed: {sol.winnerSquareGame(7)}"

    # Test 5: n=17
    assert sol.winnerSquareGame(17) is False, f"Test 5 failed: {sol.winnerSquareGame(17)}"

    # Test 6: n=3
    assert sol.winnerSquareGame(3) is True, "Test 6 failed"

    print("All tests passed for 1510. Stone Game IV!")


if __name__ == "__main__":
    run_tests()
