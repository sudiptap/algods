"""
2147. Number of Ways to Divide a Long Corridor (Hard)
https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

Given a corridor string with 'S' (seats) and 'P' (plants), place
dividers so each section has exactly 2 seats. Return number of ways
mod 10^9+7.

Pattern: Counting / Combinatorial
Approach:
- Count seat positions. If total seats is not even or < 2, return 0.
- Group seats in pairs. Between each pair of adjacent groups,
  count the number of plants (gaps). The divider can go in any of
  (gap + 1) positions between them... actually between the last seat
  of group i and first seat of group i+1, there are (gap) plant positions,
  giving (gap + 1) - wait, no. If there are g plants between the 2nd
  seat of one group and 1st seat of next group, there are g+1 positions
  for the divider.
- Wait: divider goes between two adjacent cells. If there are g plants
  between groups, divider can be in g+1 positions.
- Actually: the gap between 2nd seat of pair i and 1st seat of pair i+1
  has g positions (plants + 1 for divider placements). The divider must
  go somewhere in this gap, so there are g+1... no.
- Between the 2nd seat of pair i (at position p) and 1st seat of pair
  i+1 (at position q), the gap has q-p-1 plants. The divider can go
  at any of the q-p positions between them: after p, after p+1, ...,
  after q-1. That's q-p positions. But the divider is between two
  adjacent cells, so positions are p|p+1, p+1|p+2, ..., q-1|q.
  That's q-p positions = (gap_plants + 1).

- Multiply all gap counts together.

Time:  O(n)
Space: O(n) for seat positions
"""


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """Return number of ways to divide corridor into sections of 2 seats.

        Args:
            corridor: String of 'S' and 'P'.

        Returns:
            Count of valid divisions mod 10^9 + 7.
        """
        MOD = 10**9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']

        if len(seats) < 2 or len(seats) % 2 != 0:
            return 0

        result = 1
        # Process pairs: (seats[0],seats[1]), (seats[2],seats[3]), ...
        for i in range(2, len(seats), 2):
            # Gap between seats[i-1] and seats[i]
            gap = seats[i] - seats[i - 1]
            result = result * gap % MOD

        return result


# ---------- tests ----------
def test_number_of_ways():
    sol = Solution()

    # Example 1: "SSPPSPS" -> 3
    assert sol.numberOfWays("SSPPSPS") == 3

    # Example 2: "PPSPSP" -> 1
    assert sol.numberOfWays("PPSPSP") == 1

    # Example 3: "S" -> 0 (odd seats)
    assert sol.numberOfWays("S") == 0

    # No seats
    assert sol.numberOfWays("PPP") == 0

    # Exactly 2 seats, no division needed
    assert sol.numberOfWays("SS") == 1

    # Two pairs with plant gap: divider can go in 2 positions
    assert sol.numberOfWays("SSPSS") == 2

    print("All tests passed for 2147. Number of Ways to Divide a Long Corridor")


if __name__ == "__main__":
    test_number_of_ways()
