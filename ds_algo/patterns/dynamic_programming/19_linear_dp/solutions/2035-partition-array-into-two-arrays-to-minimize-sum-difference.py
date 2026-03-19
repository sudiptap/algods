"""
2035. Partition Array Into Two Arrays to Minimize Sum Difference (Hard)
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

Given array of 2n integers, partition into two arrays of n integers each
to minimize |sum1 - sum2|.

Pattern: Linear DP / Meet in the Middle
Approach:
- Split array into left half and right half (each of size n).
- For each half, enumerate all 2^n subsets, group by subset size k,
  and store the sum.
- For each k in [0, n], left takes k elements, right takes n-k elements.
- Sort right sums for each size. For each left sum of size k, binary
  search in right sums of size (n-k) to find closest to target.
- target = total_sum / 2. We want left_sum + right_sum closest to target
  where we pick exactly n elements total.

Time:  O(2^n * n) for enumeration + O(2^n * log(2^n)) for sorting/search
Space: O(2^n)
"""

from typing import List
from bisect import bisect_left
from collections import defaultdict


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """Return minimum |sum1 - sum2| partitioning into two equal-sized arrays.

        Args:
            nums: Array of 2n integers.

        Returns:
            Minimum absolute difference.
        """
        n = len(nums) // 2
        total = sum(nums)

        left = nums[:n]
        right = nums[n:]

        # Generate all subset sums grouped by size
        def get_sums(arr):
            m = len(arr)
            sums = defaultdict(list)
            for mask in range(1 << m):
                s = 0
                cnt = 0
                for i in range(m):
                    if mask & (1 << i):
                        s += arr[i]
                        cnt += 1
                sums[cnt].append(s)
            return sums

        left_sums = get_sums(left)
        right_sums = get_sums(right)

        # Sort right sums for binary search
        for k in right_sums:
            right_sums[k].sort()

        ans = float('inf')
        # For each k, pick k from left and n-k from right
        for k in range(n + 1):
            rk = n - k
            r_sorted = right_sums[rk]
            for ls in left_sums[k]:
                # We want ls + rs closest to total/2
                target = (total - 2 * ls) / 2
                # Binary search in r_sorted for value closest to target
                # Actually we want |total - 2*(ls+rs)| minimized
                # = |total - 2*ls - 2*rs| minimized
                # target_rs = (total - 2*ls) / 2 but that's float
                # Just minimize |total - 2*(ls + rs)|
                want = total - 2 * ls
                # Find rs closest to want/2 in r_sorted
                idx = bisect_left(r_sorted, want - want // 2)
                # Check idx and idx-1 (closest values)
                # Actually simpler: want = total - 2*(ls+rs), minimize |want - 2*rs|
                # = |total - 2*ls - 2*rs|
                # target_rs = (total - 2*ls) / 2
                target_rs = (total - 2 * ls)
                idx = bisect_left(r_sorted, target_rs / 2)
                for j in [idx - 1, idx]:
                    if 0 <= j < len(r_sorted):
                        diff = abs(total - 2 * (ls + r_sorted[j]))
                        ans = min(ans, diff)

        return ans


# ---------- tests ----------
def test_min_difference():
    sol = Solution()

    # Example 1: [3,9,7,3] -> {3,7} and {9,3}: |10-12|=2; {3,3} and {9,7}: |6-16|=10
    # Best: {3,9} and {7,3}: |12-10|=2. Or {9,3} and {3,7}: same.
    assert sol.minimumDifference([3, 9, 7, 3]) == 2

    # Example 2: [-36,36] -> only split: {-36} and {36}: diff=72
    assert sol.minimumDifference([-36, 36]) == 72

    # Example 3: [2,-1,0,4,-2,-9] -> 0
    assert sol.minimumDifference([2, -1, 0, 4, -2, -9]) == 0

    print("All tests passed for 2035. Partition Array Into Two Arrays to Minimize Sum Difference")


if __name__ == "__main__":
    test_min_difference()
