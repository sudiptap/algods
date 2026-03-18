"""
2826. Sorting Three Groups
https://leetcode.com/problems/sorting-three-groups/

Pattern: 05 - Longest Increasing Subsequence

---
APPROACH: Minimum removals = n - length of longest non-decreasing subsequence
(with values restricted to 1, 2, 3).
- dp[v] = max length of a non-decreasing subsequence ending with value v.
- For each element, it can extend any subsequence ending with value <= itself.
- dp[v] = max(dp[1], dp[2], ..., dp[v]) + 1.
- Since values are only 1, 2, 3, this runs in O(n) time.

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """Return minimum removals to make nums non-decreasing with values in {1,2,3}."""
        # dp[v] = longest non-decreasing subsequence ending with value v
        dp = [0, 0, 0, 0]  # 1-indexed: dp[1], dp[2], dp[3]

        for x in nums:
            # x can extend any subsequence ending with value <= x
            dp[x] = max(dp[1:x + 1]) + 1

        return len(nums) - max(dp[1], dp[2], dp[3])


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.minimumOperations([2, 1, 3, 2, 1]) == 3

    # Example 2
    assert sol.minimumOperations([1, 3, 2, 1, 3, 3]) == 2

    # Example 3
    assert sol.minimumOperations([2, 2, 2, 2, 3, 3]) == 0

    # Already sorted
    assert sol.minimumOperations([1, 1, 2, 2, 3, 3]) == 0

    # All same
    assert sol.minimumOperations([1, 1, 1]) == 0

    # Single element
    assert sol.minimumOperations([3]) == 0

    # Reverse sorted
    assert sol.minimumOperations([3, 2, 1]) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
