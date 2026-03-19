"""
3148. Maximum Difference Score in a Grid

Pattern: DP on Grids
Approach: Track minimum value seen above or to the left. For each cell (i,j),
    the best score ending here is grid[i][j] - min_above_or_left.
    Update min_above_or_left as we go.
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

def maxScore(grid):
    m, n = len(grid), len(grid[0])
    # mn[i][j] = min value in the region that can reach (i,j) from above/left
    mn = [[float('inf')] * n for _ in range(m)]
    ans = float('-inf')

    for i in range(m):
        for j in range(n):
            if i > 0:
                mn[i][j] = min(mn[i][j], mn[i-1][j])
            if j > 0:
                mn[i][j] = min(mn[i][j], mn[i][j-1])

            if mn[i][j] != float('inf'):  # there's a cell above/left
                ans = max(ans, grid[i][j] - mn[i][j])

            mn[i][j] = min(mn[i][j], grid[i][j])

    return ans


def test():
    assert maxScore([[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]) == 9
    assert maxScore([[4,3,2],[3,2,1]]) == -1
    print("All tests passed!")

test()
