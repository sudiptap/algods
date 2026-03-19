"""
1908. Game of Nim (Medium)
https://leetcode.com/problems/game-of-nim/

Alice and Bob play Nim. Given piles of stones, determine if Alice
(first player) wins with optimal play.

Pattern: Interval DP / Game Theory (Sprague-Grundy)
Approach:
- Classic Nim: XOR of all pile sizes.
- If XOR == 0, current player loses (second player wins).
- If XOR != 0, current player wins (first player wins).
- This is the fundamental theorem of combinatorial game theory for Nim.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        """Return True if Alice (first player) wins the Nim game.

        Args:
            piles: List of pile sizes.

        Returns:
            True if first player wins with optimal play.
        """
        xor_sum = 0
        for p in piles:
            xor_sum ^= p
        return xor_sum != 0


# ---------- tests ----------
def test_nim_game():
    sol = Solution()

    # Example 1: [1] -> XOR=1 != 0 -> Alice wins
    assert sol.nimGame([1]) is True

    # Example 2: [1,1] -> XOR=0 -> Bob wins
    assert sol.nimGame([1, 1]) is False

    # Example 3: [1,2,3] -> XOR=0 -> Bob wins
    assert sol.nimGame([1, 2, 3]) is False

    # [3,4,5] -> XOR = 3^4^5 = 2 != 0 -> Alice wins
    assert sol.nimGame([3, 4, 5]) is True

    # Single large pile
    assert sol.nimGame([100]) is True

    # [2,2] -> XOR=0 -> Bob wins
    assert sol.nimGame([2, 2]) is False

    print("All tests passed for 1908. Game of Nim")


if __name__ == "__main__":
    test_nim_game()
