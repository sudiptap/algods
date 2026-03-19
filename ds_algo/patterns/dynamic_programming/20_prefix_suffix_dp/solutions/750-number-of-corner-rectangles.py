"""
750. Number Of Corner Rectangles
https://leetcode.com/problems/number-of-corner-rectangles/

Pattern: 20 - Prefix/Suffix DP

---
APPROACH: Count column pairs with 1s in both rows
- For each pair of rows (r1, r2), count columns where both grid[r1][c]
  and grid[r2][c] are 1. If count = k, number of rectangles from this
  pair = C(k, 2) = k*(k-1)/2.
- Optimization: maintain a count map of column pairs seen so far.
  For each new row, for every pair of columns (c1, c2) both having 1,
  add the running count of that pair to the answer, then increment the pair count.

Time: O(rows * cols^2) in worst case  Space: O(cols^2)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        # For each pair of columns that both have 1 in a row,
        # track how many previous rows also had 1 in both columns.
        pair_count = defaultdict(int)
        result = 0

        for row in grid:
            ones = [c for c, val in enumerate(row) if val == 1]
            for i in range(len(ones)):
                for j in range(i + 1, len(ones)):
                    pair = (ones[i], ones[j])
                    result += pair_count[pair]
                    pair_count[pair] += 1

        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countCornerRectangles([
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ]) == 1

    assert sol.countCornerRectangles([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]) == 9  # C(3,2)*C(3,2) = 9

    assert sol.countCornerRectangles([
        [1, 1, 1, 1]
    ]) == 0  # Only one row

    assert sol.countCornerRectangles([
        [1, 1],
        [1, 1]
    ]) == 1

    assert sol.countCornerRectangles([
        [0, 0],
        [0, 0]
    ]) == 0

    print("all tests passed")
