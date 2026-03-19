"""
1755. Closest Subsequence Sum
https://leetcode.com/problems/closest-subsequence-sum/

Pattern: 19 - Linear DP

---
APPROACH: Meet in the middle
- Split array into two halves.
- Enumerate all possible subset sums for each half (2^(n/2) each).
- Sort one half's sums.
- For each sum in the first half, binary search in the second half for the
  value closest to (goal - sum1).
- This reduces 2^40 to 2 * 2^20 which is feasible.

Time: O(2^(n/2) * log(2^(n/2))) = O(n * 2^(n/2))
Space: O(2^(n/2))
---
"""

from typing import List
import bisect


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        half = n // 2

        def all_subset_sums(arr):
            sums = {0}
            for x in arr:
                sums = sums | {s + x for s in sums}
            return sorted(sums)

        left_sums = all_subset_sums(nums[:half])
        right_sums = all_subset_sums(nums[half:])

        result = float('inf')

        for s1 in left_sums:
            target = goal - s1
            idx = bisect.bisect_left(right_sums, target)
            # Check idx and idx-1
            if idx < len(right_sums):
                result = min(result, abs(s1 + right_sums[idx] - goal))
            if idx > 0:
                result = min(result, abs(s1 + right_sums[idx - 1] - goal))

        return result


# --- Tests ---
def test():
    sol = Solution()

    assert sol.minAbsDifference([5, -7, 3, 5], 6) == 0  # subset {5, -7, 3, 5} sums to 6
    assert sol.minAbsDifference([7, -9, 15, -2], -5) == 1
    assert sol.minAbsDifference([1, 2, 3], -7) == 7

    # Single element
    assert sol.minAbsDifference([5], 5) == 0
    assert sol.minAbsDifference([5], 3) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
