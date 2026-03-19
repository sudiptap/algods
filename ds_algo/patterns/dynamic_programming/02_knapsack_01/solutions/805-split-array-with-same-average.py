"""
805. Split Array With Same Average
https://leetcode.com/problems/split-array-with-same-average/

Pattern: 02 - 0/1 Knapsack

---
APPROACH: Meet in the middle with subset sums
- If arrays B (size k) and C have same average = total_sum/n,
  then sum(B)/k = total_sum/n, so sum(B)*n = total_sum*k.
- We need to find a subset of size k (1 <= k <= n/2) with
  sum(B)*n == total_sum*k.
- Normalize: subtract total_sum/n from each element. Find subset
  with sum = 0 (of any size 1..n-1).
- Meet in middle: split array in two halves, enumerate all subset
  sums for each half, check if any pair sums to 0 with total size
  in [1, n-1].

Time: O(n * 2^(n/2))  Space: O(2^(n/2))
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False

        total = sum(nums)

        # Normalize: subtract average. We look for subset sum = 0.
        # To avoid floats, multiply by n: new_val = nums[i]*n - total
        # Then we need subset sum = 0 with size k in [1, n-1].
        vals = [x * n - total for x in nums]

        # Meet in the middle
        half = n // 2
        left = vals[:half]
        right = vals[half:]

        # For left half: map sum -> set of sizes
        left_sums = defaultdict(set)
        for mask in range(1, 1 << len(left)):
            s = 0
            size = 0
            for i in range(len(left)):
                if mask & (1 << i):
                    s += left[i]
                    size += 1
            left_sums[s].add(size)

        # Check left-only subsets
        if 0 in left_sums:
            for sz in left_sums[0]:
                if 1 <= sz < n:
                    return True

        # For right half, enumerate and check complement in left
        for mask in range(1, 1 << len(right)):
            s = 0
            size = 0
            for i in range(len(right)):
                if mask & (1 << i):
                    s += right[i]
                    size += 1

            # Right-only subset
            if s == 0 and 1 <= size < n:
                return True

            # Combined with left
            complement = -s
            if complement in left_sums:
                for lsz in left_sums[complement]:
                    if 1 <= lsz + size < n:
                        return True

        return False


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]) == True
    assert sol.splitArraySameAverage([3, 1]) == False
    assert sol.splitArraySameAverage([1, 3]) == False
    assert sol.splitArraySameAverage([1, 2, 3]) == True  # [1,3] and [2] both avg 2
    assert sol.splitArraySameAverage([18, 10, 5, 3]) == False
    assert sol.splitArraySameAverage([1]) == False

    print("all tests passed")
