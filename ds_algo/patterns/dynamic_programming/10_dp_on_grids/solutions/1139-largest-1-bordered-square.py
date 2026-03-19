"""
1139. Largest 1-Bordered Square (Medium)

Pattern: 10_dp_on_grids
- Find the largest square sub-grid whose border is all 1s.

Approach:
- Precompute hor[i][j] = number of consecutive 1s ending at (i,j) going left (horizontal).
- Precompute ver[i][j] = number of consecutive 1s ending at (i,j) going up (vertical).
- For each cell (i,j), try square sizes from min(hor[i][j], ver[i][j]) down to 1.
  A square of side s with bottom-right corner at (i,j) has:
    - Bottom border: hor[i][j] >= s (already satisfied)
    - Right border: ver[i][j] >= s (already satisfied)
    - Top border: hor[i-s+1][j] >= s
    - Left border: ver[i][j-s+1] >= s
  If all four hold, we found a valid square.
- Track the maximum s found.

Complexity:
- Time:  O(m * n * min(m, n))
- Space: O(m * n)
"""

from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        hor = [[0] * n for _ in range(m)]
        ver = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hor[i][j] = (hor[i][j - 1] + 1) if j > 0 else 1
                    ver[i][j] = (ver[i - 1][j] + 1) if i > 0 else 1

        ans = 0
        for i in range(m):
            for j in range(n):
                side = min(hor[i][j], ver[i][j])
                while side > ans:
                    # Check top border and left border
                    if (hor[i - side + 1][j] >= side and
                            ver[i][j - side + 1] >= side):
                        ans = side
                        break
                    side -= 1

        return ans * ans


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.largest1BorderedSquare([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 9

    # Example 2
    assert sol.largest1BorderedSquare([[1, 1, 0, 0]]) == 1

    # All zeros
    assert sol.largest1BorderedSquare([[0, 0], [0, 0]]) == 0

    # 2x2 all ones
    assert sol.largest1BorderedSquare([[1, 1], [1, 1]]) == 4

    # Single cell
    assert sol.largest1BorderedSquare([[1]]) == 1
    assert sol.largest1BorderedSquare([[0]]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test()
