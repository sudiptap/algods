"""
801. Minimum Swaps To Make Sequences Increasing
https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

Pattern: 19 - Linear DP

---
APPROACH: Two-state DP: swap vs no-swap at each position
- no_swap[i] = min swaps to make both sequences strictly increasing up to i,
  with position i NOT swapped.
- swap[i] = min swaps with position i swapped.
- Transitions depend on whether (A[i-1]<A[i] and B[i-1]<B[i]) and/or
  (A[i-1]<B[i] and B[i-1]<A[i]):
  - If naturally increasing: no_swap[i] from no_swap[i-1], swap[i] from swap[i-1]+1
  - If cross-increasing: no_swap[i] from swap[i-1], swap[i] from no_swap[i-1]+1
- O(1) space since we only need previous values.

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        no_swap = 0  # cost if we don't swap position 0
        swap = 1     # cost if we swap position 0

        for i in range(1, n):
            new_no_swap = new_swap = float('inf')

            # If already in order without swapping at i
            if nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]:
                new_no_swap = min(new_no_swap, no_swap)
                new_swap = min(new_swap, swap + 1)

            # If in order when i and i-1 have opposite swap status
            if nums1[i - 1] < nums2[i] and nums2[i - 1] < nums1[i]:
                new_no_swap = min(new_no_swap, swap)
                new_swap = min(new_swap, no_swap + 1)

            no_swap, swap = new_no_swap, new_swap

        return min(no_swap, swap)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minSwap([1, 3, 5, 4], [1, 2, 3, 7]) == 1
    assert sol.minSwap([0, 3, 5, 8, 9], [2, 1, 4, 6, 9]) == 1
    assert sol.minSwap([0, 4, 4, 5, 9], [0, 1, 6, 8, 10]) == 1
    assert sol.minSwap([1, 2], [3, 4]) == 0

    print("all tests passed")
