"""
3251. Find the Count of Monotonic Pairs II

Pattern: Counting / Combinatorial
Approach: Same as 3250 but optimized with prefix sums to avoid inner loop.
    dp[j] with prefix sum optimization for O(n * max_val).
Time Complexity: O(n * max_val)
Space Complexity: O(max_val)
"""

def countOfPairs(nums):
    MOD = 10**9 + 7
    n = len(nums)
    max_val = max(nums)

    dp = [0] * (max_val + 1)
    for j in range(nums[0] + 1):
        dp[j] = 1

    for i in range(1, n):
        new_dp = [0] * (max_val + 1)
        prefix = [0] * (max_val + 2)
        for j in range(max_val + 1):
            prefix[j + 1] = (prefix[j] + dp[j]) % MOD

        for j in range(nums[i] + 1):
            max_prev = min(j, nums[i - 1])
            diff = nums[i] - nums[i - 1]
            if diff > 0:
                max_prev = min(max_prev, j - diff)
            if max_prev < 0:
                continue
            new_dp[j] = prefix[max_prev + 1]

        dp = new_dp

    return sum(dp) % MOD


def test():
    assert countOfPairs([2, 3, 2]) == 4
    assert countOfPairs([5, 5, 5, 5]) == 126
    print("All tests passed!")

test()
