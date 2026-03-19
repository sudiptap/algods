"""
2393. Count Strictly Increasing Subarrays
https://leetcode.com/problems/count-strictly-increasing-subarrays/

Pattern: 06 - Kadane's Pattern

---
APPROACH: Track streak length, add to total
- Maintain current streak of strictly increasing elements.
- For each element, if nums[i] > nums[i-1], streak++, else streak = 1.
- Add streak to total (each new element extends streak many subarrays).

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        total = 0
        streak = 0

        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                streak += 1
            else:
                streak = 1
            total += streak

        return total


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countSubarrays([1, 3, 5, 4, 4, 6]) == 10
    assert sol.countSubarrays([1, 2, 3, 4, 5]) == 15
    assert sol.countSubarrays([5]) == 1
    assert sol.countSubarrays([3, 3, 3]) == 3

    print("all tests passed")
