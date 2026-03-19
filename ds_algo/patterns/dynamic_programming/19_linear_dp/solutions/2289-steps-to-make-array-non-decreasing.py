"""
2289. Steps to Make Array Non-decreasing
https://leetcode.com/problems/steps-to-make-array-non-decreasing/

Pattern: 19 - Linear DP

---
APPROACH: Monotonic stack tracking steps to remove each element
- Process right to left using a stack.
- For each element, count how many steps it takes before it gets removed
  by some element to its left.
- Stack stores (value, steps). When nums[i] >= stack top value, the top
  element would be removed. The steps for removal is max of accumulated
  steps + 1 or current max.
- Answer is the maximum steps value.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []  # (value, steps_to_remove)
        ans = 0

        for i in range(len(nums) - 1, -1, -1):
            steps = 0
            while stack and nums[i] > stack[-1][0]:
                steps = max(steps + 1, stack[-1][1])
                stack.pop()
            stack.append((nums[i], steps))
            ans = max(ans, steps)

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.totalSteps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]) == 3
    assert sol.totalSteps([4, 5, 7, 7, 13]) == 0
    assert sol.totalSteps([10, 1, 2, 3, 4, 5, 6, 1, 2, 3]) == 6
    assert sol.totalSteps([5]) == 0

    print("all tests passed")
