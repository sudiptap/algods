"""
294. Flip Game II (Medium)
https://leetcode.com/problems/flip-game-ii/

You are playing Flip Game with another player. Given a string currentState
consisting only of '+' and '-', you and your opponent take turns flipping
two consecutive "++" into "--". The player who cannot make a move loses.

Return True if the first player can guarantee a win, False otherwise.

Pattern: Interval DP / Game Theory with Memoization
- Try every possible "++" -> "--" flip.
- If ANY move leaves the opponent in a losing state, the current player wins.
- Memoize on the board state string.

Time:  O(n * 2^n) worst-case with memoization (each state visited once)
Space: O(2^n) for the memo table
"""


class Solution:
    def canWin(self, currentState: str) -> bool:
        """Determine if the first player can guarantee a win.

        Args:
            currentState: String of '+' and '-' characters.

        Returns:
            True if the first player can force a win, False otherwise.
        """
        memo = {}

        def can_win(state: str) -> bool:
            if state in memo:
                return memo[state]

            for i in range(len(state) - 1):
                if state[i] == "+" and state[i + 1] == "+":
                    # Flip "++" to "--"
                    next_state = state[:i] + "--" + state[i + 2:]
                    if not can_win(next_state):
                        # Opponent loses -> current player wins
                        memo[state] = True
                        return True

            # No winning move found
            memo[state] = False
            return False

        return can_win(currentState)


# ---------- tests ----------
def test_flip_game_ii():
    sol = Solution()

    # Example 1: "++++", first player flips middle -> "--++", opponent
    # has no winning response.
    assert sol.canWin("++++") is True

    # Example 2: "+", no move possible
    assert sol.canWin("+") is False

    # Single pair "++"
    assert sol.canWin("++") is True

    # "+++" -> first player flips to "--+" or "+--", opponent has no move
    assert sol.canWin("+++") is True

    # All minus
    assert sol.canWin("---") is False

    # Empty string
    assert sol.canWin("") is False

    # Longer losing position
    assert sol.canWin("+++++") is False

    print("All tests passed for 294. Flip Game II")


if __name__ == "__main__":
    test_flip_game_ii()
