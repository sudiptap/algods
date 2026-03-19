"""
3201. Find the Maximum Length of Valid Subsequence I

Pattern: Longest Increasing Subsequence
Approach: A valid subsequence has (a[i] + a[i+1]) % 2 constant. So consecutive
    pairs sum to same value mod 2. Three cases: all even, all odd, alternating.
    Track dp by (last element mod 2, target sum mod 2).
Time Complexity: O(n)
Space Complexity: O(1)
"""

def maximumLength(nums):
    # dp[r][target] = max length of subsequence where last element % 2 == r
    # and consecutive sum % 2 == target
    # For target t: if last element mod 2 is r, next must be (t - r) % 2
    best = 0
    for target in range(2):
        dp = [0, 0]  # dp[last_mod]
        for x in nums:
            r = x % 2
            need = (target - r) % 2
            dp[r] = dp[need] + 1
            best = max(best, dp[r])
    return best


def test():
    assert maximumLength([1, 2, 3, 4]) == 4
    assert maximumLength([1, 2, 1, 1, 2, 1, 2]) == 6
    assert maximumLength([1, 3]) == 2
    print("All tests passed!")

test()
