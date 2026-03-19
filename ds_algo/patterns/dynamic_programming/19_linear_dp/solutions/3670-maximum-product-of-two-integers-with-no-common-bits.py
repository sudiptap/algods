"""
3670. Maximum Product of Two Integers With No Common Bits
https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

Pattern: 19 - Linear DP

---
APPROACH: Sort + greedy / bitmask check
- Find two numbers in array whose AND is 0 (no common bits) and
  maximize their product.
- Sort descending, check pairs greedily.
- For each pair (i,j), check nums[i] & nums[j] == 0.

Time: O(n^2) worst case, but early termination helps  Space: O(1)
---
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        best = 0

        for i in range(n):
            if nums[i] * nums[i] <= best:
                break  # can't do better
            for j in range(i + 1, n):
                if nums[i] & nums[j] == 0:
                    best = max(best, nums[i] * nums[j])
                    break  # nums sorted desc, first valid j gives max product for this i

        return best


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # [2,3,4]: 2&4=0, product=8. 3&4=0, product=12. Best=12.
    # Wait: 3=011, 4=100. 3&4=0. 12.
    res = sol.maxProduct([2, 3, 4])
    assert res == 12, f"Got {res}"

    # [1,2,3]: 1&2=0, product=2. 1&3... 01&11=01 !=0. 2&3=10&11=10!=0. Best=2.
    # Wait 2=10, 1=01. 2&1=0, product=2. But 3&0? No 0 in list.
    # Actually let me recheck: 2=10, 1=01, AND=00. product=2.
    res = sol.maxProduct([1, 2, 3])
    assert res == 2, f"Got {res}"

    print("All tests passed!")
