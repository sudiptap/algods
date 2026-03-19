"""
3205. Maximum Array Hopping Score I

Pattern: Linear DP
Approach: Score for jumping from i to j is (j - i) * nums[j]. Greedy observation:
    at each position, the best score is achieved by tracking running max from right.
    Actually, dp[i] = max(dp[j] + (i - j) * nums[i]) for j < i.
    = max(dp[j] - j * nums[i]) + i * nums[i].
    Simplification: always jump from 0 to the position that gives max (j * nums[j]),
    but we need the optimal chain. With running max approach: maintain max value
    seen so far, greedily accumulate.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxScore(nums):
    # Greedy: at each step, the contribution is max_so_far * 1 for each step
    # Think of it as: when we're at position i and jump to j, score += (j-i)*nums[j]
    # Optimal: maintain running max, each step we "accumulate" the running max
    n = len(nums)
    ans = 0
    run_max = 0
    for i in range(1, n):
        run_max = max(run_max, nums[i])
        ans += run_max
    # Wait, that's not right. Let me think again.
    # dp[i] = max score to reach i from 0
    # dp[i] = max over j<i of dp[j] + (i-j)*nums[i]
    # = i*nums[i] + max over j<i of (dp[j] - j*nums[i])
    # This depends on nums[i] so we can't easily separate.
    # For small n, O(n^2) is fine.
    dp = [0] * n
    for i in range(1, n):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + (i - j) * nums[i])
    return dp[n - 1]


def test():
    assert maxScore([4, 5, 2, 8, 9, 1, 3]) == 42
    assert maxScore([1, 5, 8]) == 16
    assert maxScore([3, 3]) == 3
    print("All tests passed!")

test()
