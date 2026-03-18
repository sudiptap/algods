"""
464. Can I Win (Medium)

Two players take turns picking from integers 1..maxChoosableInteger (without
replacement). The player whose cumulative total reaches or exceeds
desiredTotal wins. Determine if the first player can force a win assuming
both play optimally.

Approach:
    Use bitmask to represent which numbers have been used. Memoize on the
    bitmask state. For each unused number, if picking it reaches the target
    OR the opponent cannot win from the resulting state, the current player
    wins.

    Edge cases:
    - If maxChoosableInteger >= desiredTotal, first player wins immediately.
    - If the sum of all choosable integers < desiredTotal, nobody can win.

Time:  O(2^n * n)  where n = maxChoosableInteger
Space: O(2^n)
"""

from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """Return True if the first player can force a win."""
        if desiredTotal <= 0:
            return True
        if maxChoosableInteger >= desiredTotal:
            return True

        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False

        @lru_cache(maxsize=None)
        def can_win(used: int, remaining: int) -> bool:
            """Return True if the current player can force a win."""
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << i
                if used & bit:
                    continue
                # Current player picks i
                if i >= remaining:
                    return True
                # Opponent plays next; if opponent loses, current player wins
                if not can_win(used | bit, remaining - i):
                    return True
            return False

        return can_win(0, desiredTotal)


# ── Tests ──────────────────────────────────────────────────────────────────
def test_example1():
    assert Solution().canIWin(10, 11) is False

def test_example2():
    assert Solution().canIWin(10, 0) is True

def test_example3():
    assert Solution().canIWin(10, 1) is True

def test_impossible():
    # sum(1..5) = 15 < 50
    assert Solution().canIWin(5, 50) is False

def test_first_pick_wins():
    assert Solution().canIWin(5, 5) is True

def test_small_game():
    # 1..3, target 4: pick 3 → opponent picks 1 or 2, can't reach 4 alone?
    # Actually pick 1: opp needs 3 from {2,3} → picks 3 wins. pick 2: opp picks 3 wins.
    # pick 3: remaining=1, opp picks 1 wins.  So False.
    assert Solution().canIWin(3, 4) is False

def test_force_win():
    assert Solution().canIWin(4, 6) is True


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
