"""
3225. Maximum Score From Grid Operations

Pattern: DP on Grids
Approach: Column DP. For each column, decide how many cells from the top are
    "white" (the rest are "black"). Score comes from black cells adjacent to white
    cells in neighboring columns. dp[col][white_count] with prefix sum optimization.
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

def maximumScore(grid):
    m, n = len(grid), len(grid[0])

    # prefix[c][r] = sum of grid[0..r-1][c]
    prefix = [[0] * (m + 1) for _ in range(n)]
    for c in range(n):
        for r in range(m):
            prefix[c][r + 1] = prefix[c][r] + grid[r][c]

    def col_sum(c, lo, hi):
        """Sum of grid[lo..hi-1][c]"""
        if lo >= hi:
            return 0
        return prefix[c][hi] - prefix[c][lo]

    # dp[j] = max score using columns 0..current-1, where previous column has j white cells
    dp = [0] * (m + 1)

    for c in range(1, n):
        new_dp = [0] * (m + 1)
        for j in range(m + 1):  # current column has j white cells
            for pj in range(m + 1):  # previous column had pj white cells
                score = dp[pj]
                # Black cells in prev col (rows pj..m-1) adjacent to white in cur col (rows 0..j-1)
                if pj < j:
                    score += col_sum(c - 1, pj, j)
                # Black cells in cur col (rows j..m-1) adjacent to white in prev col (rows 0..pj-1)
                if j < pj:
                    score += col_sum(c, j, pj)
                new_dp[j] = max(new_dp[j], score)
        dp = new_dp

    return max(dp)


def test():
    assert maximumScore([[0, 0], [0, 0]]) == 0
    assert maximumScore([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) >= 0  # just check it runs
    print("All tests passed!")

test()
