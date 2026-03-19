"""
3256. Maximum Value Sum by Placing Three Rooks I

Pattern: Bitmask DP
Approach: For each row, find top-3 columns by value. Then try all combinations
    of 3 rows with non-conflicting columns from their top-3 picks.
Time Complexity: O(m^3 * 9) after pruning ~ O(m^3)
Space Complexity: O(m * 3)
"""

def maximumValueSum(board):
    m, n = len(board), len(board[0])

    # For each row, get top 3 (value, col) pairs
    top3 = []
    for r in range(m):
        row_vals = sorted([(board[r][c], c) for c in range(n)], reverse=True)
        top3.append(row_vals[:min(3, n)])

    ans = float('-inf')
    for r1 in range(m):
        for r2 in range(r1 + 1, m):
            for r3 in range(r2 + 1, m):
                for v1, c1 in top3[r1]:
                    for v2, c2 in top3[r2]:
                        if c2 == c1:
                            continue
                        for v3, c3 in top3[r3]:
                            if c3 == c1 or c3 == c2:
                                continue
                            ans = max(ans, v1 + v2 + v3)

    return ans


def test():
    assert maximumValueSum([[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]) == 4
    assert maximumValueSum([[1,2,3],[4,5,6],[7,8,9]]) == 15
    print("All tests passed!")

test()
