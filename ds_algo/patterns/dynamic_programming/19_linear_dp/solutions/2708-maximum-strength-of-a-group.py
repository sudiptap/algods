"""
2708. Maximum Strength of a Group
https://leetcode.com/problems/maximum-strength-of-a-group/

Pattern: 19 - Linear DP (Sort, greedy with negative pairs)

---
APPROACH: Sort the array. Pair up negatives (two negatives make positive).
Include all positives. If we have an odd number of negatives, skip the one
closest to 0. Handle edge cases: all zeros, single element.

Time: O(n log n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        negatives = [x for x in nums if x < 0]
        positives = [x for x in nums if x > 0]

        # Pair negatives
        product = 1
        used = False
        for i in range(0, len(negatives) - 1, 2):
            product *= negatives[i] * negatives[i + 1]
            used = True

        for x in positives:
            product *= x
            used = True

        if not used:
            return 0  # all zeros (and possibly one unpaired negative, but zeros dominate)

        return product


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxStrength([3, -1, -5, 2, 5, -9]) == 1350
    assert sol.maxStrength([-4, -5, -4]) == 20
    assert sol.maxStrength([0, -1]) == 0
    assert sol.maxStrength([-1]) == -1
    assert sol.maxStrength([0, 0, 0]) == 0

    print("All tests passed!")
