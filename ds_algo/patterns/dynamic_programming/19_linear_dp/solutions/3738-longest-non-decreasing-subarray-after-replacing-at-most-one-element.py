"""
3738. Longest Non-Decreasing Subarray After Replacing at Most One Element
https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/

Pattern: 19 - Linear DP

---
APPROACH: Prefix-Suffix decomposition
- left[i] = length of longest non-decreasing subarray ending at i.
- right[i] = length of longest non-decreasing subarray starting at i.
- Without replacement: max of left[i] for all i.
- With replacement at position i: if nums[i-1] <= nums[i+1], we can
  connect left[i-1] + 1 + right[i+1]. Otherwise max(left[i-1], right[i+1]) + 1.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def longestNonDecreasingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        left = [1] * n
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                left[i] = left[i - 1] + 1

        right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i + 1] >= nums[i]:
                right[i] = right[i + 1] + 1

        ans = max(left)  # no replacement

        for i in range(n):
            # Replace nums[i], connect left ending at i-1 with right starting at i+1
            l = left[i - 1] if i > 0 else 0
            r = right[i + 1] if i < n - 1 else 0

            if i == 0:
                ans = max(ans, 1 + r)
            elif i == n - 1:
                ans = max(ans, l + 1)
            elif nums[i - 1] <= nums[i + 1]:
                ans = max(ans, l + 1 + r)
            else:
                ans = max(ans, max(l, r) + 1)

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestNonDecreasingSubarray([1, 2, 3, 1, 2]) == 4
    assert sol.longestNonDecreasingSubarray([2, 2, 2, 2, 2]) == 5
    assert sol.longestNonDecreasingSubarray([1, 3, 2, 4]) == 4   # replace 2 with 3: [1,3,3,4]
    assert sol.longestNonDecreasingSubarray([5, 1]) == 2          # replace either
    assert sol.longestNonDecreasingSubarray([1]) == 1

    print("all tests passed")
