"""
2547. Minimum Cost to Split an Array
https://leetcode.com/problems/minimum-cost-to-split-an-array/

Pattern: 19 - Linear DP

---
APPROACH: Linear DP with frequency tracking
- dp[i] = minimum cost to split nums[0..i-1] into subarrays.
- For each position i, try all split points j (start of last subarray):
    dp[i] = min over j in [0..i-1] of (dp[j] + importance(nums[j..i-1]) + k)
- importance(subarray) = number of elements that appear more than once
  (sum of freq for elements with freq >= 2), which we call trimmedLength.
- We maintain a frequency map as we extend j backward to efficiently
  compute importance without recomputing from scratch.

Time:  O(n^2)
Space: O(n)
---
"""

from typing import List


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        """Return the minimum cost to split nums into subarrays.

        Cost of a subarray = k + (number of elements with frequency >= 2 in that subarray,
        counting each such element freq times). We call this the trimmed length + k.
        """
        n = len(nums)
        # dp[i] = min cost for nums[0..i-1]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            freq = {}
            importance = 0
            dp[i] = float("inf")
            # Try all starting positions j for the last subarray nums[j..i-1]
            for j in range(i - 1, -1, -1):
                val = nums[j]
                freq[val] = freq.get(val, 0) + 1
                if freq[val] == 2:
                    # This element just became "important" — count both occurrences
                    importance += 2
                elif freq[val] > 2:
                    # One more occurrence of an already-important element
                    importance += 1
                dp[i] = min(dp[i], dp[j] + importance + k)

        return dp[n]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.minCost([1, 2, 1, 2, 1, 3, 3], 2) == 8
    # Example 2
    assert sol.minCost([1, 2, 1, 2, 1], 2) == 6
    # Example 3
    assert sol.minCost([1, 2, 1, 2, 1], 5) == 10
    # Single element
    assert sol.minCost([1], 1) == 1
    # All same elements
    assert sol.minCost([5, 5, 5], 2) == 5
    # All distinct
    assert sol.minCost([1, 2, 3], 3) == 3

    print("Solution: all tests passed")
