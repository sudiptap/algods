"""
1931. Painting a Grid With Three Different Colors (Hard)
https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

Paint an m x n grid with 3 colors such that no two adjacent cells share
the same color. Return the number of ways mod 10^9+7.

Pattern: Counting / Combinatorial (State Compression)
Approach:
- m is small (<=5). Represent each column as a tuple of m colors.
- Generate all valid column colorings (no two adjacent in same column
  share a color).
- Build transition: two columns are compatible if no same-row cells
  share a color.
- dp[col_state] = number of ways to color up to current column ending
  with col_state.
- Iterate over n columns, multiplying by transition.

Time:  O(n * S^2) where S = valid column states (at most 3*2^(m-1) = 48 for m=5)
Space: O(S)
"""


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """Return number of valid 3-color paintings of an m x n grid.

        Args:
            m: Number of rows.
            n: Number of columns.

        Returns:
            Count of valid paintings mod 10^9 + 7.
        """
        MOD = 10**9 + 7

        # Generate all valid column colorings
        def gen_columns(m):
            if m == 1:
                return [[c] for c in range(3)]
            result = []
            for col in gen_columns(m - 1):
                for c in range(3):
                    if c != col[-1]:
                        result.append(col + [c])
            return result

        columns = [tuple(c) for c in gen_columns(m)]

        # Check if two columns are compatible (no same color in same row)
        def compatible(c1, c2):
            return all(a != b for a, b in zip(c1, c2))

        # Precompute transitions
        transitions = {}
        for c in columns:
            transitions[c] = [c2 for c2 in columns if compatible(c, c2)]

        # DP
        dp = {c: 1 for c in columns}

        for _ in range(n - 1):
            new_dp = {}
            for c2 in columns:
                total = 0
                for c1 in transitions[c2]:
                    total += dp.get(c1, 0)
                new_dp[c2] = total % MOD
            dp = new_dp

        return sum(dp.values()) % MOD


# ---------- tests ----------
def test_color_the_grid():
    sol = Solution()

    # Example 1: m=1, n=1 -> 3
    assert sol.colorTheGrid(1, 1) == 3

    # Example 2: m=1, n=2 -> 6
    assert sol.colorTheGrid(1, 2) == 6

    # Example 3: m=5, n=5 -> 580986
    assert sol.colorTheGrid(5, 5) == 580986

    # m=2, n=1 -> 6 (3*2)
    assert sol.colorTheGrid(2, 1) == 6

    print("All tests passed for 1931. Painting a Grid With Three Different Colors")


if __name__ == "__main__":
    test_color_the_grid()
