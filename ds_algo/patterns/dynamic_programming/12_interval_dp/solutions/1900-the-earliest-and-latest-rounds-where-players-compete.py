"""
1900. The Earliest and Latest Rounds Where Players Compete (Hard)
https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

n players in a tournament. In each round, players pair up from the ends.
The stronger player wins. Given firstPlayer and secondPlayer (1-indexed)
who always win against others, find the earliest and latest round they
can compete against each other.

Pattern: Interval DP / Memoized Simulation
Approach:
- State: (n, i, j) = total players, positions of first and second player
  (0-indexed from left).
- In each round, players at positions k and (n-1-k) compete.
- If i and (n-1-j) match (i.e., i + j == n-1), they compete this round.
- Otherwise, enumerate all possible outcomes for other matches.
  Track new positions of our two players after the round.
- Memoize to avoid recomputation.

Time:  O(n^4) per state with small constants
Space: O(n^3)
"""

from typing import List
from functools import lru_cache


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        """Return [earliest, latest] round the two players compete.

        Args:
            n: Number of players.
            firstPlayer: 1-indexed position of first player.
            secondPlayer: 1-indexed position of second player.

        Returns:
            [earliest round, latest round].
        """
        # Convert to 0-indexed; ensure i < j
        fp, sp = firstPlayer - 1, secondPlayer - 1

        @lru_cache(maxsize=None)
        def solve(n, i, j):
            # i, j are 0-indexed positions, i < j
            if i + j == n - 1:
                return (1, 1)

            half = n // 2
            earliest = float('inf')
            latest = 0

            # After this round, half players survive (ceil(n/2))
            survivors = (n + 1) // 2

            # Enumerate possible new positions for i and j
            # Players at positions k and n-1-k are paired.
            # For k < n-1-k, winner takes position k in the next round's
            # lineup of survivors.
            # i is at position i, j is at position j.
            # i is paired with n-1-i, j is paired with n-1-j.
            # Since i < j, we know i != j.
            # Also i + j != n-1 (checked above), so they don't face each other.

            # Count players before i, between i and j, after j that could
            # either win or lose their match.
            # For pairs entirely before both i,j or after both, the winner
            # can be either player.

            # Let's think about it differently:
            # After the round, survivors keep relative order.
            # i competes with n-1-i. Since i < j and i+j < n-1 or i+j > n-1:
            # Case 1: i + j < n - 1 (both in first half, or i in first half, j also)
            #   i pairs with n-1-i (which is > j since n-1-i > j means i+j < n-1)
            #   j pairs with n-1-j (which is < i since n-1-j < i means i+j > n-1... contradiction)
            #   Actually let's just enumerate.

            # New positions depend on how many players before them survive.
            # Let's enumerate: for each pair (k, n-1-k) where k < n-1-k,
            # and neither k nor n-1-k is i or j, we choose who wins.
            # i always wins their pair, j always wins their pair.

            # Pairs: (0, n-1), (1, n-2), ..., (half-1, n-half)
            # If n is odd, middle player (n//2) auto-advances.

            # Collect "free" pairs (neither endpoint is i or j)
            free_pairs = []
            i_pair = n - 1 - i  # opponent of i
            j_pair = n - 1 - j  # opponent of j

            for k in range(half):
                partner = n - 1 - k
                if k == i or k == j or partner == i or partner == j:
                    continue
                # This is a free pair; winner could be at position k or partner
                free_pairs.append((k, partner))

            # For each subset of free pairs (choose which side wins),
            # compute new positions of i and j among survivors.
            def enumerate_outcomes(idx, survivor_positions):
                nonlocal earliest, latest
                if idx == len(free_pairs):
                    # Add i and j (they always survive)
                    all_survivors = sorted(survivor_positions + [i, j])
                    # If n is odd, add middle
                    new_n = len(all_survivors)
                    new_i = all_survivors.index(i)
                    new_j = all_survivors.index(j)
                    # Map to 0-indexed positions in new round
                    e, l = solve(new_n, new_i, new_j)
                    earliest = min(earliest, e)
                    latest = max(latest, l)
                    return

                k, partner = free_pairs[idx]
                # Winner is k (lower position)
                enumerate_outcomes(idx + 1, survivor_positions + [k])
                # Winner is partner (higher position)
                enumerate_outcomes(idx + 1, survivor_positions + [partner])

            # Start: add survivors that are fixed (not free, not i/j)
            fixed = []
            if n % 2 == 1:
                mid = n // 2
                if mid != i and mid != j:
                    fixed.append(mid)

            # i wins against i_pair, j wins against j_pair
            # But we need to handle when i_pair or j_pair might overlap with other pairs
            enumerate_outcomes(0, fixed)

            return (earliest + 1, latest + 1)

        return list(solve(n, fp, sp))


# ---------- tests ----------
def test_earliest_latest():
    sol = Solution()

    # Example 1
    assert sol.earliestAndLatest(11, 2, 4) == [3, 4]

    # Example 2
    assert sol.earliestAndLatest(5, 1, 5) == [1, 1]

    # n=2, players 1 and 2
    assert sol.earliestAndLatest(2, 1, 2) == [1, 1]

    # n=3, players 1 and 3 (they pair in round 1)
    assert sol.earliestAndLatest(3, 1, 3) == [1, 1]

    print("All tests passed for 1900. Earliest and Latest Rounds")


if __name__ == "__main__":
    test_earliest_latest()
