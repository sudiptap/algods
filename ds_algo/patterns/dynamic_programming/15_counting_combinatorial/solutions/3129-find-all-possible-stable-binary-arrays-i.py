"""
3129. Find All Possible Stable Binary Arrays I

Pattern: Counting / Combinatorial
Approach: dp[i][j][last] = number of stable binary arrays using i zeros and j ones,
    ending with 'last' (0 or 1). No more than 'limit' consecutive same elements.
    Use prefix-sum subtraction: dp0[i][j] = dp0[i-1][j] + dp1[i-1][j] - dp1[i-1-limit][j].
Time Complexity: O(zero * one)
Space Complexity: O(zero * one)
"""

def numberOfStableArrays(zero, one, limit):
    MOD = 10**9 + 7

    # dp0[i][j] = arrays with i zeros, j ones, ending with 0
    # dp1[i][j] = arrays with i zeros, j ones, ending with 1
    dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
    dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

    # Base cases: sequences of just zeros or just ones
    for i in range(1, min(zero, limit) + 1):
        dp0[i][0] = 1
    for j in range(1, min(one, limit) + 1):
        dp1[0][j] = 1

    for i in range(1, zero + 1):
        for j in range(1, one + 1):
            # Ending with 0: previous was 1 (any run), or extend run of 0s
            # dp0[i][j] = dp0[i-1][j] + dp1[i-1][j]
            # But subtract cases where we'd have limit+1 consecutive 0s:
            # That means positions i-limit..i are all 0, so position i-limit-1 must end with 1
            # dp0[i][j] -= dp1[i-1-limit][j] if i-1-limit >= 0
            dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD
            if i - 1 - limit >= 0:
                dp0[i][j] = (dp0[i][j] - dp1[i-1-limit][j]) % MOD

            # Ending with 1: symmetric
            dp1[i][j] = (dp1[i][j-1] + dp0[i][j-1]) % MOD
            if j - 1 - limit >= 0:
                dp1[i][j] = (dp1[i][j] - dp0[i][j-1-limit]) % MOD

    return (dp0[zero][one] + dp1[zero][one]) % MOD


def test():
    assert numberOfStableArrays(1, 1, 2) == 2
    assert numberOfStableArrays(1, 2, 1) == 1
    assert numberOfStableArrays(3, 3, 2) == 14
    print("All tests passed!")

test()
