"""
2770. Maximum Number of Jumps to Reach the Last Index
https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

Pattern: 19 - Linear DP (dp[i] = max jumps to reach i)

---
APPROACH: dp[i] = max number of jumps to reach index i. For each i, check
all j < i where |nums[i] - nums[j]| <= target (i.e., -target <= nums[i]-nums[j] <= target).

Time: O(n^2)  Space: O(n)
---
"""

from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if dp[j] >= 0 and abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumJumps([1, 3, 6, 4, 1, 2], 2) == 3
    assert sol.maximumJumps([1, 3, 6, 4, 1, 2], 3) == 5
    assert sol.maximumJumps([1, 3, 6, 4, 1, 2], 0) == -1

    print("All tests passed!")
