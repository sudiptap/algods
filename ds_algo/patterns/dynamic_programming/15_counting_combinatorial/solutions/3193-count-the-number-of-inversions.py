"""
3193. Count the Number of Inversions

Pattern: Counting / Combinatorial
Approach: dp[group][inv] = number of ways to arrange groups 0..group with exactly
    inv inversions, subject to requirements constraints. For each new group position,
    it can create 0 to group inversions with existing elements.
Time Complexity: O(n^2 * max_inversions)
Space Complexity: O(n * max_inversions)
"""

def numberOfPermutations(n, requirements):
    MOD = 10**9 + 7
    req = {}
    for end, cnt in requirements:
        req[end] = cnt

    max_inv = max(cnt for _, cnt in requirements)

    # dp[i][j] = number of permutations of 0..i with exactly j inversions
    # When adding element i+1, it can be placed at any of i+1 positions,
    # creating 0 to i new inversions
    dp = [[0] * (max_inv + 1) for _ in range(n)]

    # Base: permutation of [0], 0 inversions
    if 0 in req:
        if req[0] == 0:
            dp[0][0] = 1
        # else impossible
    else:
        dp[0][0] = 1

    for i in range(1, n):
        for j in range(max_inv + 1):
            # Adding element i (0-indexed) to permutation of 0..i-1
            # It can create k new inversions, k in [0, i]
            # dp[i][j] = sum of dp[i-1][j-k] for k in [0, min(i, j)]
            for k in range(min(i, j) + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD

        # Apply requirement constraint
        if i in req:
            target = req[i]
            for j in range(max_inv + 1):
                if j != target:
                    dp[i][j] = 0

    # Answer: dp[n-1][req[n-1]] but n-1 must be in requirements
    if n - 1 in req:
        return dp[n - 1][req[n - 1]]
    return sum(dp[n - 1]) % MOD


def test():
    assert numberOfPermutations(3, [[2, 2], [0, 0]]) == 2
    assert numberOfPermutations(3, [[2, 3]]) == 1  # [2,1,0] only
    assert numberOfPermutations(2, [[1, 0]]) == 1  # [0,1]
    print("All tests passed!")

test()
