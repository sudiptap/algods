"""
2750. Ways to Split Array Into Good Subarrays
https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

Pattern: 19 - Linear DP (Count gaps between 1s, multiply)

---
APPROACH: Each good subarray has exactly one 1. Between consecutive 1s at
positions p1 and p2, we can place the split at any of (p2 - p1) positions.
Multiply all gap sizes. If no 1s exist, answer is 0.

Time: O(n)  Space: O(1)
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        prev = -1
        result = 1
        found = False

        for i, x in enumerate(nums):
            if x == 1:
                if prev >= 0:
                    result = result * (i - prev) % MOD
                prev = i
                found = True

        return result if found else 0


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfGoodSubarraySplits([0, 1, 0, 0, 1]) == 3
    assert sol.numberOfGoodSubarraySplits([0, 1, 0]) == 1
    assert sol.numberOfGoodSubarraySplits([0, 0, 0]) == 0

    print("All tests passed!")
