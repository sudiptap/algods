"""
2811. Check if it is Possible to Split Array
https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

Pattern: 19 - Linear DP (Greedy: any adjacent pair with sum >= m works)

---
APPROACH: For n <= 2, always possible. For n >= 3, we need at least one
adjacent pair with sum >= m. Because we can always reduce to that pair last.

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        for i in range(n - 1):
            if nums[i] + nums[i + 1] >= m:
                return True
        return False


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.canSplitArray([2, 2, 1], 4) == True
    assert sol.canSplitArray([2, 1, 3], 5) == False
    assert sol.canSplitArray([2, 3, 3, 2, 3], 6) == True

    print("All tests passed!")
