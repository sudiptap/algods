"""
1659. Maximize Grid Happiness
https://leetcode.com/problems/maximize-grid-happiness/

Pattern: 11 - Bitmask DP

---
APPROACH: Profile DP (cell by cell)
- Grid is m x n where n <= 5. Process cell by cell, left to right, top to bottom.
- State: (position, introverts_left, extroverts_left, profile)
  where profile is a tuple of n values representing what was placed in the
  n cells directly above/left of current position (sliding window of last n cells).
- Each cell can be: empty(0), introvert(1), extrovert(2).
- For each cell, try placing nothing, introvert, or extrovert.
- Compute adjacency bonuses/penalties from top and left neighbors.

Time: O(m * n * introvertsCount * extrovertsCount * 3^n)
Space: O(same for memoization)
---
"""

from functools import lru_cache


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:

        def get_cost(person, neighbor):
            """Get happiness change when person is adjacent to neighbor."""
            if person == 0 or neighbor == 0:
                return 0
            cost = 0
            if person == 1:  # introvert loses 30 per neighbor
                cost -= 30
            else:  # extrovert gains 20 per neighbor
                cost += 20
            if neighbor == 1:
                cost -= 30
            else:
                cost += 20
            return cost

        @lru_cache(maxsize=None)
        def solve(pos, intro_left, extro_left, profile):
            if pos == m * n:
                return 0
            row, col = divmod(pos, n)

            top = profile[col] if row > 0 else 0
            left = profile[col - 1] if col > 0 else 0

            best = float('-inf')

            for person in [0, 1, 2]:
                if person == 1 and intro_left == 0:
                    continue
                if person == 2 and extro_left == 0:
                    continue

                gain = 0
                if person == 1:
                    gain = 120
                elif person == 2:
                    gain = 40

                if person != 0:
                    gain += get_cost(person, top)
                    if col > 0:
                        gain += get_cost(person, left)

                new_intro = intro_left - (1 if person == 1 else 0)
                new_extro = extro_left - (1 if person == 2 else 0)

                new_profile = list(profile)
                new_profile[col] = person
                val = gain + solve(pos + 1, new_intro, new_extro, tuple(new_profile))
                best = max(best, val)

            return best

        return solve(0, introvertsCount, extrovertsCount, tuple([0] * n))


# --- Tests ---
def test():
    sol = Solution()

    assert sol.getMaxGridHappiness(2, 3, 1, 2) == 240
    assert sol.getMaxGridHappiness(3, 1, 2, 1) == 260
    assert sol.getMaxGridHappiness(2, 2, 4, 0) == 240

    print("All tests passed!")


if __name__ == "__main__":
    test()
