"""
2369. Check if There is a Valid Partition For The Array
https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

Pattern: 19 - Linear DP

---
APPROACH:
dp[i] = True if nums[:i] can be validly partitioned.
For each position i (1-indexed length), check:
  1. Pair (equal):       dp[i-2] and nums[i-1] == nums[i-2]
  2. Triple (equal):     dp[i-3] and nums[i-1] == nums[i-2] == nums[i-3]
  3. Triple (consec):    dp[i-3] and nums[i-1] == nums[i-2]+1 == nums[i-3]+2

Base: dp[0] = True (empty prefix is valid).

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        """Return True if the array has at least one valid partition."""
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(2, n + 1):
            # Check pair: two equal elements
            if nums[i - 1] == nums[i - 2] and dp[i - 2]:
                dp[i] = True
            # Check triple: three equal elements
            if i >= 3 and nums[i - 1] == nums[i - 2] == nums[i - 3] and dp[i - 3]:
                dp[i] = True
            # Check triple: three consecutive increasing
            if (
                i >= 3
                and nums[i - 1] == nums[i - 2] + 1 == nums[i - 3] + 2
                and dp[i - 3]
            ):
                dp[i] = True

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: [4,4,4,5,6] -> True (triple equal [4,4,4] + triple consec [4,5,6])
    assert sol.validPartition([4, 4, 4, 5, 6]) is True
    # Example 2: [1,1,1,2] -> False
    assert sol.validPartition([1, 1, 1, 2]) is False
    # Two equal elements
    assert sol.validPartition([3, 3]) is True
    # Three consecutive
    assert sol.validPartition([1, 2, 3]) is True
    # Three equal
    assert sol.validPartition([7, 7, 7]) is True
    # Single element - can't partition
    # (constraint says n>=2, but [1] would be False)

    print("all tests passed")
