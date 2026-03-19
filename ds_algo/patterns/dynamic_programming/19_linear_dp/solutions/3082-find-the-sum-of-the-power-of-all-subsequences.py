"""
3082. Find the Sum of the Power of All Subsequences

Pattern: Linear DP
Approach: dp[j][k] where j = current sum target, k = subsequence length.
    The power of a subsequence of length L that sums to target contributes
    2^(n-L) to the answer (other elements can be in or out).
    dp[j][k] = number of subsequences of length k summing to j.
    Answer = sum over k of dp[target][k] * 2^(n-k).
Time Complexity: O(n * k * target)
Space Complexity: O(n * target)
"""

def sumOfPower(nums, k):
    MOD = 10**9 + 7
    n = len(nums)
    # dp[j][l] = number of subsequences of length l summing to j
    # Optimize: we only need the sum contribution, so track dp[j] weighted by 2^(-l)
    # Actually: answer = sum_l dp[k][l] * 2^(n-l)
    # = 2^n * sum_l dp[k][l] * 2^(-l)
    # So define dp2[j] = sum_l (count of subseq of length l summing to j) * (1/2)^l
    # Multiply by 2^n at the end.

    # Use modular inverse of 2
    inv2 = pow(2, MOD - 2, MOD)

    # dp[j] = sum over all subsequences summing to j of inv2^(length)
    dp = [0] * (k + 1)
    dp[0] = 1  # empty subsequence, length 0, inv2^0 = 1

    for x in nums:
        # Process in reverse to avoid using same element twice
        for j in range(k, x - 1, -1):
            dp[j] = (dp[j] + dp[j - x] * inv2) % MOD

    return dp[k] * pow(2, n, MOD) % MOD


def test():
    assert sumOfPower([1, 2, 3], 3) == 6
    assert sumOfPower([2, 3, 3], 5) == 4
    assert sumOfPower([1, 2, 3], 7) == 0
    print("All tests passed!")

test()
