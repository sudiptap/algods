"""
689. Maximum Sum of 3 Non-Overlapping Subarrays
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

Pattern: 06 - Kadane's Pattern

---
APPROACH: Prefix sums + left/right best window indices
- Compute window sums for all windows of size k.
- left[i] = index of best (max sum) window starting at or before i.
- right[i] = index of best (max sum) window starting at or after i.
- For each middle window starting at j (k <= j <= n-2k),
  combine left[j-k] + window[j] + right[j+k] and track max.
- left scanned left-to-right (use >= for leftmost), right scanned right-to-left (use >= for rightmost tiebreak gives lexicographically smallest).

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        num_windows = n - k + 1

        # Compute window sums
        w = [0] * num_windows
        s = sum(nums[:k])
        w[0] = s
        for i in range(1, num_windows):
            s += nums[i + k - 1] - nums[i - 1]
            w[i] = s

        # left[i] = index of max window sum in w[0..i]
        left = [0] * num_windows
        best = 0
        for i in range(num_windows):
            if w[i] > w[best]:
                best = i
            left[i] = best

        # right[i] = index of max window sum in w[i..end]
        right = [0] * num_windows
        best = num_windows - 1
        for i in range(num_windows - 1, -1, -1):
            if w[i] >= w[best]:  # >= to prefer leftmost (smallest index)
                best = i
            right[i] = best

        # Find best triple
        ans = [-1, -1, -1]
        max_total = 0
        for j in range(k, num_windows - k):
            li, ri = left[j - k], right[j + k]
            total = w[li] + w[j] + w[ri]
            if total > max_total:
                max_total = total
                ans = [li, j, ri]

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2) == [0, 3, 5]
    assert sol.maxSumOfThreeSubarrays([1, 2, 1, 2, 1, 2, 1, 2, 1], 2) == [0, 2, 4]
    assert sol.maxSumOfThreeSubarrays([4, 5, 10, 6, 11, 17, 4, 11, 1, 3], 1) == [4, 5, 7]
    assert sol.maxSumOfThreeSubarrays([7, 13, 20, 19, 19, 2, 10, 1, 1, 19], 3) == [1, 4, 7]

    print("all tests passed")
