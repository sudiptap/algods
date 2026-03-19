"""
488. Zuma Game (Hard)
https://leetcode.com/problems/zuma-game/

Pattern: Linear DP / BFS + DFS with Pruning

Given a string board of colored balls and a string hand of balls
you can insert, find the minimum number of balls to insert to clear
the board. Three or more consecutive same-colored balls are removed.
Return -1 if impossible.

Approach:
    DFS with pruning:
    1. Remove all groups of 3+ consecutive balls from the board.
    2. For each position in the board, try inserting each ball from hand
       adjacent to a same-colored ball (pruning: only insert next to
       matching colors, or insert to make a pair).
    3. Recurse and track minimum insertions.

Time:  Exponential but heavily pruned
Space: O(board * hand) for recursion
"""

from functools import lru_cache


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        """Return min balls to insert to clear the board, or -1."""

        def remove_consecutive(s: str) -> str:
            """Remove all groups of 3+ consecutive same chars."""
            while True:
                new_s = ""
                i = 0
                removed = False
                while i < len(s):
                    j = i
                    while j < len(s) and s[j] == s[i]:
                        j += 1
                    if j - i >= 3:
                        removed = True
                    else:
                        new_s += s[i:j]
                    i = j
                s = new_s
                if not removed:
                    break
            return s

        sorted_hand = "".join(sorted(hand))

        @lru_cache(maxsize=None)
        def dfs(board: str, hand: str) -> int:
            if not board:
                return 0
            if not hand:
                return float("inf")

            best = float("inf")
            i = 0
            while i < len(board):
                j = i
                while j < len(board) and board[j] == board[i]:
                    j += 1
                # Group board[i:j] has color board[i], count = j - i
                color = board[i]
                need = 3 - (j - i)  # balls needed to pop this group

                # Check if hand has enough of this color
                count_in_hand = hand.count(color)
                if count_in_hand >= need:
                    # Use 'need' balls of this color from hand
                    new_hand = hand
                    for _ in range(need):
                        idx = new_hand.index(color)
                        new_hand = new_hand[:idx] + new_hand[idx + 1:]
                    new_board = remove_consecutive(board[:i] + board[j:])
                    result = dfs(new_board, new_hand)
                    if result != float("inf"):
                        best = min(best, need + result)

                i = j

            return best

        result = dfs(board, sorted_hand)
        return result if result != float("inf") else -1


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().findMinStep("WRRBBW", "RB") == -1

def test_example2():
    assert Solution().findMinStep("WWRRBBWW", "WRBRW") == 2

def test_example3():
    assert Solution().findMinStep("G", "GGGGG") == 2

def test_already_empty():
    assert Solution().findMinStep("", "RRR") == 0

def test_single_color():
    assert Solution().findMinStep("RR", "R") == 1

def test_no_hand():
    # Board "RRR" is given as-is; with empty hand we cannot act on it
    # but the problem guarantees no initial 3+ groups, so test a realistic case
    assert Solution().findMinStep("RR", "") == -1


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
