"""
3836. Maximum Score Using Exactly K Pairs
https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

Pattern: 19 - Linear DP

---
APPROACH: Sort + DP selecting k pairs
- Given nums1 (length n) and nums2 (length m), choose exactly k pairs (i,j)
  where each index from nums1 and nums2 is used at most once.
- Score of a pair (i,j) = nums1[i] + nums2[j].
- Maximize total score of k pairs.
- Greedy: sort both arrays descending, pick top k from each.
  Score = sum of top k from nums1 + sum of top k from nums2.
  This works because pairing doesn't matter for the sum - any pairing
  of the top k from each gives the same total.

Time: O(n log n + m log m)  Space: O(1)
---
"""

from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1_sorted = sorted(nums1, reverse=True)
        nums2_sorted = sorted(nums2, reverse=True)

        return sum(nums1_sorted[:k]) + sum(nums2_sorted[:k])


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Basic tests
    assert sol.maxScore([1, 2, 3], [4, 5, 6], 2) == (3 + 2) + (6 + 5)  # top 2 from each
    assert sol.maxScore([1], [1], 1) == 2
    assert sol.maxScore([3, 1, 2], [5, 4], 1) == 3 + 5

    print("all tests passed")
