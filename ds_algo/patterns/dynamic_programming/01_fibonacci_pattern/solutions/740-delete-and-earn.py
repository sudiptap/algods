"""
740. Delete and Earn (Medium)

You are given an integer array nums. You want to maximize the number of points
you get by performing the following operation any number of times:
- Pick any nums[i] and delete it to earn nums[i] points.
- You must also delete every element equal to nums[i]-1 and nums[i]+1.

Pattern: Fibonacci / House Robber reduction
- Aggregate points per value: points[v] = v * count(v).
- Choosing value v forbids v-1 and v+1, identical to House Robber on
  consecutive values.
- dp[i] = max(dp[i-1], dp[i-2] + points[i])

Time:  O(n + max_val)
Space: O(max_val)
"""

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """Return the maximum points earned by deleting elements."""
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num

        # House Robber on the points array
        prev2, prev1 = 0, 0
        for i in range(1, max_val + 1):
            prev2, prev1 = prev1, max(prev1, prev2 + points[i])

        return prev1


# ----------------- Tests -----------------
def run_tests():
    sol = Solution()

    # Example 1: delete 3's -> earn 3+3 = 6, 2's removed; then earn nothing more
    # Actually: delete all 3s to earn 9, 2 and 4 removed. But only [3,4,2] here.
    assert sol.deleteAndEarn([3, 4, 2]) == 6, "Test 1 failed"

    # Example 2: delete 3,3 -> earn 6, then 1,1 -> earn 2, total 8
    assert sol.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9, "Test 2 failed"

    # Single element
    assert sol.deleteAndEarn([5]) == 5, "Test 3 failed"

    # All same elements
    assert sol.deleteAndEarn([3, 3, 3]) == 9, "Test 4 failed"

    # Non-adjacent values (can take all)
    assert sol.deleteAndEarn([1, 3, 5, 7]) == 16, "Test 5 failed"

    # Two adjacent values
    assert sol.deleteAndEarn([1, 1, 2, 2]) == 4, "Test 6 failed"

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
