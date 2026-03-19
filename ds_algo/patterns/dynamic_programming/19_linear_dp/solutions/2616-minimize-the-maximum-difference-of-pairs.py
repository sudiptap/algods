"""
2616. Minimize the Maximum Difference of Pairs
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

Pattern: 19 - Linear DP (Binary Search + Greedy)

---
APPROACH: Binary search on the answer (max difference). For a given threshold,
greedily pair adjacent elements (after sorting) if their diff <= threshold.
Count how many pairs we can form.

Time: O(n log n + n log(max_val))  Space: O(1)
---
"""

from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        def can_form(threshold):
            count = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= threshold:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p

        lo, hi = 0, nums[-1] - nums[0] if n > 1 else 0
        while lo < hi:
            mid = (lo + hi) // 2
            if can_form(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimizeMax([10, 1, 2, 7, 1, 3], 2) == 1
    assert sol.minimizeMax([4, 2, 1, 2], 1) == 0
    assert sol.minimizeMax([0, 5, 3, 4], 0) == 0

    print("All tests passed!")
