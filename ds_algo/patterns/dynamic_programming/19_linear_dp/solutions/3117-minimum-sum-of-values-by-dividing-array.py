"""
3117. Minimum Sum of Values by Dividing Array

Pattern: Linear DP
Approach: dp[i][j] = min sum using first i elements of nums split into first j
    groups, where AND of each group equals andValues[j-1]. Use the property that
    AND only decreases as we include more elements. Binary search or sliding window
    to find valid ranges.
Time Complexity: O(n * m * log(n)) with optimizations
Space Complexity: O(n * m)
"""
from functools import lru_cache

def minimumValueSum(nums, andValues):
    n, m = len(nums), len(andValues)

    @lru_cache(maxsize=None)
    def dp(i, j, cur_and):
        """i = index in nums, j = index in andValues, cur_and = running AND of current group"""
        if i == n and j == m:
            return 0
        if i == n or j == m:
            return float('inf')

        cur_and &= nums[i]

        # If cur_and < andValues[j], AND can only decrease, so prune
        if cur_and < andValues[j]:
            return float('inf')

        # Option 1: extend current group
        res = dp(i + 1, j, cur_and)

        # Option 2: end current group here (if AND matches)
        if cur_and == andValues[j]:
            sub = dp(i + 1, j + 1, (1 << 30) - 1)
            if sub != float('inf'):
                res = min(res, nums[i] + sub)

        return res

    ans = dp(0, 0, (1 << 30) - 1)
    return ans if ans != float('inf') else -1


def test():
    assert minimumValueSum([1, 4, 3, 3, 2], [0, 3, 3, 2]) == 12
    assert minimumValueSum([2, 3, 5, 7, 7, 7, 5], [0, 7, 5]) == 17
    assert minimumValueSum([1, 2, 3, 4], [2]) == -1
    print("All tests passed!")

test()
