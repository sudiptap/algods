"""
3830. Longest Alternating Subarray After Removing At Most One Element
https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/

Pattern: 06 - Kadane's Pattern

---
APPROACH: Prefix-Suffix decomposition with 0/1 removal
- Alternating: adjacent comparisons alternate between > and <.
- l1[i] = longest alternating subarray ending at i where last comparison is <.
- l2[i] = longest alternating subarray ending at i where last comparison is >.
- r1[i] = longest starting at i where first comparison is <.
- r2[i] = longest starting at i where first comparison is >.
- Without removal: max of all l1[i], l2[i].
- With removal at position i: try connecting l2[i-1] + r2[i+1] (if nums[i-1] < nums[i+1])
  or l1[i-1] + r1[i+1] (if nums[i-1] > nums[i+1]).

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        # l1[i]: length of longest alternating ending at i, last step was up (<)
        # l2[i]: last step was down (>)
        l1 = [1] * n
        l2 = [1] * n
        ans = 1

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                l1[i] = l2[i - 1] + 1
            elif nums[i - 1] > nums[i]:
                l2[i] = l1[i - 1] + 1
            ans = max(ans, l1[i], l2[i])

        # r1[i]: length starting at i, first step is up (nums[i] < nums[i+1])
        # r2[i]: first step is down
        r1 = [1] * n
        r2 = [1] * n

        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                r1[i] = r2[i + 1] + 1
            elif nums[i + 1] < nums[i]:
                r2[i] = r1[i + 1] + 1

        # Try removing each element i
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i + 1]:
                # After removing i: ...nums[i-1] < nums[i+1]...
                # Need: ending at i-1 with last step down, starting at i+1 with first step down
                ans = max(ans, l2[i - 1] + r2[i + 1])
            elif nums[i - 1] > nums[i + 1]:
                ans = max(ans, l1[i - 1] + r1[i + 1])

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestAlternating([2, 1, 3, 2]) == 4
    assert sol.longestAlternating([3, 2, 1, 2, 3, 2, 1]) == 4
    assert sol.longestAlternating([100000, 100000]) == 1
    assert sol.longestAlternating([1, 2, 1, 2, 1]) == 5
    assert sol.longestAlternating([1, 3, 2, 4, 3]) == 5

    print("all tests passed")
