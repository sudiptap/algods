"""
377. Combination Sum IV (Medium)

Given an array of distinct integers nums and a target, return the number of
possible combinations that add up to target. Different orderings count as
different combinations (i.e., this is really a permutation count).

Pattern: Unbounded Knapsack.

Approach:
    dp[i] = number of ways to reach sum i using the given nums.
    For each sum i from 1 to target, try every num:
        if i >= num:  dp[i] += dp[i - num]

    Iterating over sums in the outer loop (rather than items) naturally
    counts different orderings as distinct, which is what the problem asks.

Time:  O(target * len(nums))
Space: O(target)
"""

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """Return the number of ordered combinations that sum to target."""
        dp = [0] * (target + 1)
        dp[0] = 1  # one way to make sum 0: use nothing

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]


# ───────────────────────── Tests ─────────────────────────
def test():
    s = Solution()

    # Example 1
    assert s.combinationSum4([1, 2, 3], 4) == 7

    # Target 0 -> 1 way (empty combination)
    assert s.combinationSum4([1, 2, 3], 0) == 1

    # Single element repeated
    assert s.combinationSum4([2], 4) == 1   # only [2,2]
    assert s.combinationSum4([2], 3) == 0   # impossible

    # Single element = 1
    assert s.combinationSum4([1], 5) == 1   # only [1,1,1,1,1]

    # Two elements
    assert s.combinationSum4([1, 2], 4) == 5  # 1111, 112, 121, 211, 22

    # Larger target
    assert s.combinationSum4([1, 2, 3], 5) == 13

    print("All tests passed for 377!")


if __name__ == "__main__":
    test()
