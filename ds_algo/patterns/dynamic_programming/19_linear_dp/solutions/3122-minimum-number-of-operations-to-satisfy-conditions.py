"""
3122. Minimum Number of Operations to Satisfy Conditions

Pattern: Linear DP
Approach: For each column, count frequency of each digit 0-9. For each column,
    pick a digit (all cells become that digit). Adjacent columns must have different
    digits. dp per column: dp[col][d] = min ops for columns 0..col with column col
    having digit d. Cost to make column c all digit d = m - count[c][d].
Time Complexity: O(n * m + n * 100) ~ O(n * m)
Space Complexity: O(n * 10)
"""

def minimumOperations(grid):
    m, n = len(grid), len(grid[0])

    # Count frequency of each digit in each column
    freq = [[0] * 10 for _ in range(n)]
    for r in range(m):
        for c in range(n):
            freq[c][grid[r][c]] += 1

    # Cost to make column c all digit d
    cost = [[m - freq[c][d] for d in range(10)] for c in range(n)]

    # dp[d] = min total cost for columns 0..current with current column = d
    prev = [cost[0][d] for d in range(10)]

    for c in range(1, n):
        curr = [0] * 10
        # Precompute best and second best from prev
        best1_val, best1_d = float('inf'), -1
        best2_val = float('inf')
        for d in range(10):
            if prev[d] < best1_val:
                best2_val = best1_val
                best1_val, best1_d = prev[d], d
            elif prev[d] < best2_val:
                best2_val = prev[d]

        for d in range(10):
            if d != best1_d:
                curr[d] = cost[c][d] + best1_val
            else:
                curr[d] = cost[c][d] + best2_val
        prev = curr

    return min(prev)


def test():
    assert minimumOperations([[1, 0, 2], [1, 0, 2]]) == 0
    assert minimumOperations([[1, 1, 1], [0, 0, 0]]) == 3
    assert minimumOperations([[1], [2], [3]]) == 2
    print("All tests passed!")

test()
