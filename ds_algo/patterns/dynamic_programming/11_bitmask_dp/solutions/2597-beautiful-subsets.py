"""
2597. The Number of Beautiful Subsets
https://leetcode.com/problems/the-number-of-beautiful-subsets/

Pattern: 11 - Bitmask DP (Backtracking / Group by mod k + House Robber)

---
APPROACH: Group elements by (val % k). Within each group, sort and apply
house-robber-style counting: elements differing by exactly k cannot coexist.
For each group, count subsets via DP. Multiply across groups and subtract 1
for the empty subset.

Time: O(n log n)  Space: O(n)
---
"""

from typing import List
from collections import Counter


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups = {}
        for x in nums:
            r = x % k
            groups.setdefault(r, []).append(x)

        result = 1
        for r, vals in groups.items():
            freq = Counter(vals)
            sorted_vals = sorted(freq.keys())
            # dp: number of subsets for this group (including empty)
            prev_no, prev_yes = 1, 0
            for i, v in enumerate(sorted_vals):
                cnt = freq[v]
                ways = (1 << cnt) - 1  # non-empty subsets of this value
                if i > 0 and v - sorted_vals[i - 1] == k:
                    # conflict with previous
                    new_no = prev_no + prev_yes
                    new_yes = prev_no * ways
                else:
                    new_no = prev_no + prev_yes
                    new_yes = (prev_no + prev_yes) * ways
                prev_no, prev_yes = new_no, new_yes
            result *= (prev_no + prev_yes)

        return result - 1  # subtract empty subset


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.beautifulSubsets([2, 4, 6], 2) == 4
    assert sol.beautifulSubsets([1], 1) == 1
    assert sol.beautifulSubsets([1, 2, 3, 3], 1) == 8
    assert sol.beautifulSubsets([10, 4, 5, 7, 2, 1], 3) == 23

    print("All tests passed!")
