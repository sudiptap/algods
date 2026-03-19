"""
3840. House Robber V
https://leetcode.com/problems/house-robber-v/

Pattern: 01 - Fibonacci Pattern (House Robber variant)

---
APPROACH: DP with color-based adjacency constraint
- Cannot rob two adjacent houses that share the same color.
- If adjacent houses have different colors, you CAN rob both.
- dp[i] = max money robbing from houses 0..i.
- If colors[i] != colors[i-1]: dp[i] = max(dp[i-1], dp[i-1] + nums[i])
  = dp[i-1] + nums[i] (always rob since no constraint).
  Wait, that's not right. The constraint is: you cannot rob two adjacent
  houses IF they share the same color. So if different colors, you can
  rob both adjacent houses.
- dp[i] = max money considering houses 0..i where we decide to rob or skip i.
- rob[i] = max money if we rob house i.
- skip[i] = max money if we skip house i.
- skip[i] = max(rob[i-1], skip[i-1])
- rob[i]:
  - If colors[i] == colors[i-1]: can't rob both, so rob[i] = skip[i-1] + nums[i]
  - If colors[i] != colors[i-1]: rob[i] = max(rob[i-1], skip[i-1]) + nums[i]

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def houseRobber(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        rob = nums[0]
        skip = 0

        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                new_rob = skip + nums[i]
            else:
                new_rob = max(rob, skip) + nums[i]
            new_skip = max(rob, skip)
            rob, skip = new_rob, new_skip

        return max(rob, skip)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.houseRobber([1, 4, 3, 5], [1, 1, 2, 2]) == 9  # houses 1,3: 4+5
    assert sol.houseRobber([3, 1, 2, 4], [2, 3, 2, 2]) == 8  # houses 0,1,3: 3+1+4
    assert sol.houseRobber([5], [1]) == 5
    assert sol.houseRobber([1, 2, 3], [1, 2, 3]) == 6  # all different colors, rob all
    assert sol.houseRobber([1, 2, 3], [1, 1, 1]) == 4  # same color, classic house robber

    print("all tests passed")
