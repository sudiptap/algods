"""
845. Longest Mountain in Array
https://leetcode.com/problems/longest-mountain-in-array/

Pattern: 06 - Kadane's Pattern

---
APPROACH: Track up/down lengths in single pass
- Maintain up and down counters.
- If arr[i] > arr[i-1] and down == 0: up += 1 (still ascending)
- If arr[i] < arr[i-1]: down += 1 (descending)
- If arr[i] == arr[i-1] or (arr[i] > arr[i-1] and down > 0):
  reset, start new potential mountain.
- A valid mountain has up > 0 and down > 0. Length = up + down + 1.

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        result = 0
        up = 0
        down = 0

        for i in range(1, n):
            # Reset conditions: flat or going up after going down
            if (down > 0 and arr[i] > arr[i - 1]) or arr[i] == arr[i - 1]:
                up = 0
                down = 0

            if arr[i] > arr[i - 1]:
                up += 1
            elif arr[i] < arr[i - 1]:
                down += 1

            if up > 0 and down > 0:
                result = max(result, up + down + 1)

        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestMountain([2, 1, 4, 7, 3, 2, 5]) == 5  # [1,4,7,3,2]
    assert sol.longestMountain([2, 2, 2]) == 0
    assert sol.longestMountain([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == 11
    assert sol.longestMountain([0, 1, 0]) == 3
    assert sol.longestMountain([1, 2, 3]) == 0  # no descent
    assert sol.longestMountain([3, 2, 1]) == 0  # no ascent
    assert sol.longestMountain([]) == 0

    print("all tests passed")
