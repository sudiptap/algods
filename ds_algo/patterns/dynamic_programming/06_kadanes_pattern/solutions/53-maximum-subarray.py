"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Pattern: 06 - Kadane's Pattern (THE classic problem for this pattern)

---
APPROACH 1: Kadane's Algorithm
- At each index: either extend the current subarray or start fresh
- current_sum = max(nums[i], current_sum + nums[i])
- Track global max

Time: O(n)  Space: O(1)

APPROACH 2: Divide and Conquer (follow-up)
- Split array in half, answer is in left, right, or crossing the midpoint
- Crossing: extend left from mid, extend right from mid+1, combine

Time: O(n log n)  Space: O(log n) recursion
---
"""

from typing import List


# ---------- Approach 1: Kadane's ----------
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            # key decision: extend or restart
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


# ---------- Approach 2: Divide and Conquer ----------
class SolutionDC:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            # max crossing subarray: must include mid and mid+1
            left_sum = float('-inf')
            curr = 0
            for i in range(mid, left - 1, -1):
                curr += nums[i]
                left_sum = max(left_sum, curr)

            right_sum = float('-inf')
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                right_sum = max(right_sum, curr)

            cross = left_sum + right_sum

            return max(helper(left, mid), helper(mid + 1, right), cross)

        return helper(0, len(nums) - 1)


# ---------- Tests ----------
if __name__ == "__main__":
    for Sol in [Solution, SolutionDC]:
        sol = Sol()

        assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
        assert sol.maxSubArray([1]) == 1
        assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
        assert sol.maxSubArray([-1]) == -1
        assert sol.maxSubArray([-2, -1]) == -1
        assert sol.maxSubArray([1, 2, 3]) == 6

        print(f"{Sol.__name__}: all tests passed")
