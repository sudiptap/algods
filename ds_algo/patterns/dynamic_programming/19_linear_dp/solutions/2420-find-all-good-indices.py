"""
2420. Find All Good Indices
https://leetcode.com/problems/find-all-good-indices/

Pattern: 19 - Linear DP

---
APPROACH: Prefix non-increasing + suffix non-decreasing
- Precompute dec[i] = length of non-increasing run ending at i.
- Precompute inc[i] = length of non-decreasing run starting at i.
- Index i is good if dec[i-1] >= k and inc[i+1] >= k.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # dec[i] = length of non-increasing run ending at index i
        dec = [1] * n
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                dec[i] = dec[i - 1] + 1

        # inc[i] = length of non-decreasing run starting at index i
        inc = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                inc[i] = inc[i + 1] + 1

        result = []
        for i in range(k, n - k):
            if dec[i - 1] >= k and inc[i + 1] >= k:
                result.append(i)

        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.goodIndices([2,1,1,1,3,4,1], 2) == [2, 3]
    assert sol.goodIndices([2,1,1,2], 2) == []
    assert sol.goodIndices([1,1,1,1,1], 1) == [1, 2, 3]

    print("all tests passed")
