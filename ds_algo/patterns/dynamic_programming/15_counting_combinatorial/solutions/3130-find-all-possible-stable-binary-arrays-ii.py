"""
3130. Find All Possible Stable Binary Arrays II

Pattern: Counting / Combinatorial
Approach: Same DP as 3129. dp0[i][j] and dp1[i][j] with modular arithmetic.
Time Complexity: O(zero * one)
Space Complexity: O(zero * one)
"""

def numberOfStableArrays(zero, one, limit):
    MOD = 10**9 + 7
    dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
    dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

    for i in range(1, min(zero, limit) + 1):
        dp0[i][0] = 1
    for j in range(1, min(one, limit) + 1):
        dp1[0][j] = 1

    for i in range(1, zero + 1):
        for j in range(1, one + 1):
            dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD
            if i - 1 - limit >= 0:
                dp0[i][j] = (dp0[i][j] - dp1[i-1-limit][j]) % MOD

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
