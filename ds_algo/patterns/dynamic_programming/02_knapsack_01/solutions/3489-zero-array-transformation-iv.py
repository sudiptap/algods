"""
3489. Zero Array Transformation IV
https://leetcode.com/problems/zero-array-transformation-iv/

Pattern: 02 - 0/1 Knapsack (Binary search + knapsack)

---
APPROACH: Binary search on k (number of queries to use). For each k, check if we can
make all elements zero using the first k queries.
- Each query [l, r, val]: can subtract val from any subset of positions in [l, r].
- For each position i: need to find subset of queries covering i whose vals sum to nums[i].
- This is a knapsack per position: can we select from applicable queries to sum to nums[i]?
- Binary search on k, then for each position run a bitset knapsack.

Time: O(n * k * max_val) with binary search  Space: O(max_val)
---
"""

from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)

        def canMakeZero(k):
            """Check if using first k queries can zero out nums."""
            for i in range(n):
                if nums[i] == 0:
                    continue
                target = nums[i]
                # Collect queries covering position i
                applicable = []
                for j in range(k):
                    l, r, val = queries[j]
                    if l <= i <= r:
                        applicable.append(val)
                # Knapsack: can we sum to target from applicable values?
                # Use bitset DP
                dp = 1 << 0  # bit 0 is set (sum 0 is achievable)
                for v in applicable:
                    dp |= dp << v
                if not (dp >> target) & 1:
                    return False
            return True

        # Binary search
        if all(x == 0 for x in nums):
            return 0

        lo, hi = 1, m
        if not canMakeZero(m):
            return -1

        while lo < hi:
            mid = (lo + hi) // 2
            if canMakeZero(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minZeroArray([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]]) == 2
    assert sol.minZeroArray([4, 3, 2, 1], [[1, 3, 2], [0, 2, 1]]) == -1
    assert sol.minZeroArray([0, 0, 0], [[1, 2, 1]]) == 0

    print("Solution: all tests passed")
