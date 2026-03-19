"""
2638. Count the Number of K-Free Subsets
https://leetcode.com/problems/count-the-number-of-k-free-subsets/

Pattern: 19 - Linear DP (Group by mod k, House Robber counting)

---
APPROACH: A k-free subset has no two elements differing by exactly k.
Group elements by val % k. Within each group, sort and apply house-robber
counting: if consecutive group elements differ by k, they conflict.
f(i) = subsets including/excluding element i. Multiply across groups.

Time: O(n log n)  Space: O(n)
---
"""

from typing import List
from collections import Counter


class Solution:
    def countTheNumberOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        groups = {}
        for x in nums:
            groups.setdefault(x % k, []).append(x)

        result = 1
        for r, vals in groups.items():
            vals.sort()
            # House robber: skip = subsets not taking current, take = subsets taking current
            skip, take = 1, 1  # start: can take or skip first element
            for i in range(1, len(vals)):
                if vals[i] - vals[i - 1] == k:
                    new_skip = skip + take
                    new_take = skip
                    skip, take = new_skip, new_take
                else:
                    # No conflict, both can extend freely
                    skip, take = skip + take, skip + take
            result *= (skip + take)

        return result


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countTheNumberOfKFreeSubsets([5, 4, 6], 1) == 5
    assert sol.countTheNumberOfKFreeSubsets([2, 3, 5, 8], 5) == 12
    assert sol.countTheNumberOfKFreeSubsets([10, 5, 9, 11], 20) == 16

    print("All tests passed!")
