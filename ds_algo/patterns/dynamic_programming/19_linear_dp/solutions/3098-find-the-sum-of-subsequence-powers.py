"""
3098. Find the Sum of Subsequence Powers

Pattern: Linear DP
Approach: Sort array, then dp with state (index, count_remaining, last_picked, min_diff).
    Use memoization. The "power" of a subsequence is the minimum absolute difference
    between any two elements. After sorting, min diff is between consecutive picked elements.
Time Complexity: O(n^2 * k * D) where D is number of distinct diffs
Space Complexity: O(n^2 * k * D)
"""
from functools import lru_cache

def sumOfPowers(nums, k):
    MOD = 10**9 + 7
    nums.sort()
    n = len(nums)

    # Collect all possible differences to limit state space
    @lru_cache(maxsize=None)
    def dp(i, rem, last, min_diff):
        """i=current index, rem=elements still to pick, last=index of last picked, min_diff=min diff so far"""
        if rem == 0:
            return min_diff % MOD
        if i == n:
            return 0
        if n - i < rem:
            return 0

        # Skip i
        res = dp(i + 1, rem, last, min_diff)
        # Pick i
        new_diff = min_diff
        if last != -1:
            new_diff = min(new_diff, nums[i] - nums[last])
        res = (res + dp(i + 1, rem - 1, i, new_diff)) % MOD
        return res

    return dp(0, k, -1, float('inf'))


def test():
    assert sumOfPowers([1, 2, 3, 4], 3) == 4
    assert sumOfPowers([4, 3, 2, 1], 2) == 10
    print("All tests passed!")

test()
