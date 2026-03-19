"""
3040. Maximum Number of Operations With the Same Score II

Pattern: Interval DP
Approach: Memoized DFS. Each operation removes 2 elements from either end (both left,
    both right, or one from each). The score must remain the same throughout.
    Try all 3 possible first-move scores, then DFS with memoization on (l, r).
Time Complexity: O(n^2) per score attempt
Space Complexity: O(n^2)
"""
from functools import lru_cache

def maxOperations(nums):
    n = len(nums)

    def solve(target):
        @lru_cache(maxsize=None)
        def dp(l, r):
            if r - l + 1 < 2:
                return 0
            res = 0
            # Take both left
            if nums[l] + nums[l + 1] == target:
                res = max(res, 1 + dp(l + 2, r))
            # Take both right
            if nums[r] + nums[r - 1] == target:
                res = max(res, 1 + dp(l, r - 2))
            # Take one from each end
            if nums[l] + nums[r] == target:
                res = max(res, 1 + dp(l + 1, r - 1))
            return res

        result = dp(0, n - 1)
        dp.cache_clear()
        return result

    # Try all 3 possible first-move scores
    targets = set()
    if n >= 2:
        targets.add(nums[0] + nums[1])
        targets.add(nums[-1] + nums[-2])
        targets.add(nums[0] + nums[-1])

    return max(solve(t) for t in targets) if targets else 0


def test():
    assert maxOperations([3, 2, 1, 2, 3, 4]) == 3
    assert maxOperations([3, 2, 6, 1, 4]) == 2
    assert maxOperations([1, 2]) == 1
    print("All tests passed!")

test()
