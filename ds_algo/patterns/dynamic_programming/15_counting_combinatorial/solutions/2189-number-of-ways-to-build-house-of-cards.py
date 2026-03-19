"""
2189. Number of Ways to Build House of Cards (Medium)
https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

Given n cards, build a house of cards. Each row of width w uses 3w-1 cards
(w triangles need 2w cards for triangles + w-1 cards for ceilings).
Return number of ways to build.

Pattern: Counting / Combinatorial DP
Approach:
- A row of width w uses 3*w - 1 cards and must be wider than the row above.
- dp[cards_remaining][max_width] = number of ways.
- Try each possible bottom row width, subtract cards used, recurse with
  remaining cards and smaller max width.
- Actually: dp[n] = ways to use exactly n cards.
  For each possible bottom row width w (using 3w-1 cards), the remaining
  n - (3w-1) cards build on top with width < w.
- dp(cards, max_w): ways to use exactly 'cards' cards with rows of width <= max_w.

Time:  O(n^2) roughly
Space: O(n^2) for memoization
"""

from functools import lru_cache


class Solution:
    def houseOfCards(self, n: int) -> int:
        """Return number of ways to build a house of cards with n cards.

        Args:
            n: Number of cards.

        Returns:
            Number of valid house-of-cards structures.
        """

        @lru_cache(maxsize=None)
        def dp(remaining, max_width):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0

            count = 0
            # Don't place any more rows (only valid if remaining == 0, handled above)
            # Try each row width from 1 to max_width
            for w in range(1, max_width + 1):
                cards_used = 3 * w - 1
                if cards_used > remaining:
                    break
                # Next row must be strictly smaller
                count += dp(remaining - cards_used, w - 1)

            return count

        # Maximum possible width
        max_w = (n + 1) // 3  # 3w - 1 <= n -> w <= (n+1)/3
        return dp(n, max_w)


# ---------- tests ----------
def test_house_of_cards():
    sol = Solution()

    # Example 1: n=16 -> 2
    assert sol.houseOfCards(16) == 2

    # Example 2: n=2 -> 1 (one triangle)
    assert sol.houseOfCards(2) == 1

    # Example 3: n=4 -> 0
    assert sol.houseOfCards(4) == 0

    # n=1 -> 0
    assert sol.houseOfCards(1) == 0

    # n=5 -> 1 (row of width 2: uses 5 cards)
    assert sol.houseOfCards(5) == 1

    # n=7 -> 1 (row of width 2 + row of width 1: 5+2=7)
    assert sol.houseOfCards(7) == 1

    print("All tests passed for 2189. Number of Ways to Build House of Cards")


if __name__ == "__main__":
    test_house_of_cards()
