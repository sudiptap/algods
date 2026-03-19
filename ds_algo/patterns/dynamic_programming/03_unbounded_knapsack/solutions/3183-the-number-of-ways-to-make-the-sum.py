"""
3183. The Number of Ways to Make the Sum

Pattern: Unbounded Knapsack
Approach: Classic coin change counting. Coins are [1, 2, 6] (since we can use
    1, 2, and 6 = denomination coins). Standard unbounded knapsack DP.
    dp[j] += dp[j - coin] for each coin.
Time Complexity: O(n * k) where k = number of coin types
Space Complexity: O(n)
"""

def numberOfWays(n):
    MOD = 10**9 + 7
    coins = [1, 2, 6]
    dp = [0] * (n + 1)
    dp[0] = 1

    for coin in coins:
        for j in range(coin, n + 1):
            dp[j] = (dp[j] + dp[j - coin]) % MOD

    return dp[n]


def test():
    # Coins {1,2,6}: 4 = {1111, 112, 22} = 3 ways
    assert numberOfWays(4) == 3
    assert numberOfWays(12) == 12
    assert numberOfWays(5) == 3
    print("All tests passed!")

test()
