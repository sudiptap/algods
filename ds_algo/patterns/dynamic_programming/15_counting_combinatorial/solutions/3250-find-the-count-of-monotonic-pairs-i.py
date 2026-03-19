"""
3250. Find the Count of Monotonic Pairs I

Pattern: Counting / Combinatorial
Approach: dp[i][j] = number of valid pairs where arr1[i] = j.
    arr1 is non-decreasing, arr2 = nums - arr1 is non-increasing.
    Constraint: arr1[i] + arr2[i] = nums[i], 0 <= arr1[i] <= nums[i].
    arr1 non-decreasing: arr1[i] >= arr1[i-1].
    arr2 non-increasing: nums[i] - arr1[i] <= nums[i-1] - arr1[i-1]
    => arr1[i] - arr1[i-1] >= nums[i] - nums[i-1].
Time Complexity: O(n * max_val^2)
Space Complexity: O(max_val)
"""

def countOfPairs(nums):
    MOD = 10**9 + 7
    n = len(nums)
    max_val = max(nums)

    # dp[j] = count of valid arrays with arr1[current] = j
    dp = [0] * (max_val + 1)
    for j in range(nums[0] + 1):
        dp[j] = 1

    for i in range(1, n):
        new_dp = [0] * (max_val + 1)
        prefix = [0] * (max_val + 2)
        for j in range(max_val + 1):
            prefix[j + 1] = (prefix[j] + dp[j]) % MOD

        for j in range(nums[i] + 1):
            # arr1[i] = j, arr1[i-1] <= j
            # Also: j - arr1[i-1] >= nums[i] - nums[i-1]
            # => arr1[i-1] <= j - (nums[i] - nums[i-1])
            # And arr1[i-1] <= nums[i-1]
            max_prev = min(j, nums[i - 1])
            if nums[i] > nums[i - 1]:
                max_prev = min(max_prev, j - (nums[i] - nums[i - 1]))

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
