"""
2681. Power of Heroes
https://leetcode.com/problems/power-of-heroes/

Pattern: 19 - Linear DP (Sort, prefix sum contribution)

---
APPROACH: Sort nums. For each element as max of a subsequence, sum contributions
of all possible mins. After sorting, for nums[i] as max, each nums[j] (j<=i)
as min contributes nums[j] * 2^(i-j-1) (number of subsets of elements between).
Track running prefix S = sum(nums[j] * 2^(i-j-1)) efficiently.

Time: O(n log n)  Space: O(1)
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        prefix = 0  # sum of nums[j] * 2^(i-j-1) for j < i
        for x in nums:
            # x as both min and max (subset = {x}): x^2 * x = x^3
            # x as max, with some earlier element as min: x^2 * prefix
            ans = (ans + x * x % MOD * (x + prefix)) % MOD
            prefix = (2 * prefix + x) % MOD
        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.sumOfPower([2, 1, 4]) == 141
    assert sol.sumOfPower([1, 1, 1]) == 7

    print("All tests passed!")
