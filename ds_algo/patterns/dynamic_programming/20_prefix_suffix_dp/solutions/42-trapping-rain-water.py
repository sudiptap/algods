"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Pattern: 20 - Prefix/Suffix DP (also: Two Pointers)

---
Core insight: Water at index i = min(max_left[i], max_right[i]) - height[i]
The water level at any bar is bounded by the shorter of the tallest walls on each side.

APPROACH 1: Prefix/Suffix arrays
- Precompute left_max[i] = max(height[0..i])
- Precompute right_max[i] = max(height[i..n-1])
- Water at i = min(left_max[i], right_max[i]) - height[i]

Time: O(n)  Space: O(n)

APPROACH 2: Two Pointers (optimal)
- left, right pointers moving inward
- Track left_max and right_max
- Key: if left_max <= right_max, we KNOW water at left is bounded by left_max
  (because right side has something >= right_max >= left_max)
  So process left pointer. Vice versa.

Time: O(n)  Space: O(1)
---
"""

from typing import List


# ---------- Approach 1: Prefix/Suffix DP ----------
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water


# ---------- Approach 2: Two Pointers ----------
class SolutionTwoPointers:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        left, right = 0, n - 1
        left_max, right_max = height[0], height[n - 1]
        water = 0

        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water


# ---------- Tests ----------
if __name__ == "__main__":
    for Sol in [Solution, SolutionTwoPointers]:
        sol = Sol()

        assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
        assert sol.trap([4, 2, 0, 3, 2, 5]) == 9
        assert sol.trap([1, 2, 3, 4, 5]) == 0       # ascending, no trap
        assert sol.trap([5, 4, 3, 2, 1]) == 0       # descending, no trap
        assert sol.trap([3, 0, 3]) == 3
        assert sol.trap([]) == 0
        assert sol.trap([1]) == 0

        print(f"{Sol.__name__}: all tests passed")
