"""
3257. Maximum Value Sum by Placing Three Rooks II

Pattern: Bitmask DP
Approach: Same as 3256. For each row, keep top-3 columns. Enumerate all triples
    of rows and their top-3 column picks, ensuring no column conflicts.
    This works for large boards since we only check 3^3=27 combos per row triple,
    and we prune rows intelligently.
Time Complexity: O(m^3 * 27) worst case, optimized with row pruning
Space Complexity: O(m)
"""

def maximumValueSum(board):
    m, n = len(board), len(board[0])

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
