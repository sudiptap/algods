"""
3202. Find the Maximum Length of Valid Subsequence II

Pattern: Longest Increasing Subsequence
Approach: Generalization of 3201. Consecutive pair sums are constant mod k.
    For each target t in [0, k), track dp[r] = max length of subsequence with
    last element mod k == r and pair sum mod k == t.
Time Complexity: O(n * k)
Space Complexity: O(k)
"""

def maximumLength(nums, k):
    best = 0
    for target in range(k):
        dp = [0] * k
        for x in nums:
            r = x % k
            need = (target - r) % k
            dp[r] = dp[need] + 1
            best = max(best, dp[r])
    return best


def test():
    assert maximumLength([1, 2, 3, 4, 5], 2) == 5
    assert maximumLength([1, 4, 2, 3, 1, 4], 3) == 4
    print("All tests passed!")

test()
