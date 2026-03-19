"""
2436. Minimum Split Into Subarrays With GCD Greater Than One
https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

Pattern: 19 - Linear DP (Greedy)

---
APPROACH: Greedy - extend current subarray while GCD > 1
- Maintain running GCD of current subarray.
- When GCD becomes 1, start a new subarray from current element.
- This greedy works because extending never makes GCD larger, and starting
  new subarrays earlier only increases the count.

Time: O(n * log(max_val))  Space: O(1)
---
"""

from typing import List
from math import gcd


class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        splits = 1
        cur_gcd = nums[0]

        for i in range(1, len(nums)):
            new_gcd = gcd(cur_gcd, nums[i])
            if new_gcd > 1:
                cur_gcd = new_gcd
            else:
                splits += 1
                cur_gcd = nums[i]

        return splits


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumSplits([12, 6, 3, 14, 8]) == 2
    assert sol.minimumSplits([4, 12, 6, 14]) == 1
    assert sol.minimumSplits([1, 2, 1]) == 3
    assert sol.minimumSplits([7]) == 1

    print("all tests passed")
