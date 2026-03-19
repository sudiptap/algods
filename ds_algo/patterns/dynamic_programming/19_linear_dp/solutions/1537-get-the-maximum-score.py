"""
1537. Get the Maximum Score
https://leetcode.com/problems/get-the-maximum-score/

Pattern: 19 - Linear DP

---
APPROACH: Two pointers on sorted arrays, split at common values
- Both arrays are sorted. Use two pointers to traverse them.
- At common values (intersection points), take the max of accumulated sums
  from both paths, then continue.
- Between intersections, each pointer accumulates its own sum independently.
- At each intersection, we pick the better path so far and reset.

Time: O(n + m) where n, m = lengths of nums1, nums2
Space: O(1)
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        sum1, sum2 = 0, 0

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                # Common value - take max path and reset
                sum1 = sum2 = max(sum1, sum2) + nums1[i]
                i += 1
                j += 1

        # Collect remaining
        while i < n:
            sum1 += nums1[i]
            i += 1
        while j < m:
            sum2 += nums2[j]
            j += 1

        return max(sum1, sum2) % MOD


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.maxSum([2, 4, 5, 8, 10], [4, 6, 8, 9]) == 30
    # Path: 2->4->5->8->10 gives 2+4+5+8+10=29; 2->4->6->8->10=30

    # Example 2
    assert sol.maxSum([1, 3, 5, 7, 9], [3, 5, 100]) == 109
    # 1->3->5->100 = 109

    # Example 3
    assert sol.maxSum([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == 40

    # No common elements
    assert sol.maxSum([1, 3, 5], [2, 4, 6]) == 12  # max(9, 12)

    # Single elements
    assert sol.maxSum([1], [1]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    test()
