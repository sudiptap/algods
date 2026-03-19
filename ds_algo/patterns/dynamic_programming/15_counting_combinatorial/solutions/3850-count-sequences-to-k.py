"""
3850. Count Sequences to K
https://leetcode.com/problems/count-sequences-to-k/

Pattern: 15 - Counting / Combinatorial DP

---
APPROACH: DP tracking all reachable rational values
- Start with val=1. For each nums[i], choose: multiply, divide, or skip.
- Division is exact (rational), not integer division.
- Track val as a fraction (numerator, denominator) in reduced form.
- Count sequences where final val == k.
- Use dict mapping (num, den) -> count of ways to reach that state.

Time: O(n * S) where S = number of distinct rational states
Space: O(S)
---
"""

from typing import List
from math import gcd
from collections import defaultdict


class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def normalize(num, den):
            """Normalize fraction to canonical form."""
            if den < 0:
                num, den = -num, -den
            g = gcd(abs(num), den)
            return (num // g, den // g)

        # dp: dict of (numerator, denominator) -> count
        dp = defaultdict(int)
        dp[(1, 1)] = 1  # start with val=1

        for x in nums:
            new_dp = defaultdict(int)
            for (num, den), cnt in dp.items():
                if cnt == 0:
                    continue
                # Option 1: multiply by x
                new_num, new_den = normalize(num * x, den)
                new_dp[(new_num, new_den)] = (new_dp[(new_num, new_den)] + cnt) % MOD

                # Option 2: divide by x
                new_num2, new_den2 = normalize(num, den * x)
                new_dp[(new_num2, new_den2)] = (new_dp[(new_num2, new_den2)] + cnt) % MOD

                # Option 3: leave unchanged
                new_dp[(num, den)] = (new_dp[(num, den)] + cnt) % MOD

            dp = new_dp

        target = normalize(k, 1)
        return dp.get(target, 0)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.countSequences([2, 3, 2], 6) == 2
    assert sol.countSequences([1], 1) == 3  # multiply/divide/skip all give 1
    assert sol.countSequences([2], 2) == 1  # only multiply
    # [2], k=1: multiply->2, divide->1/2, skip->1. Only skip gives 1.
    assert sol.countSequences([2], 1) == 1

    print("all tests passed")
