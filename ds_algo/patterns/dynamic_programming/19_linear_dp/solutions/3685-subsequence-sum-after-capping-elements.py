"""
3685. Subsequence Sum After Capping Elements
https://leetcode.com/problems/subsequence-sum-after-capping-elements/

Pattern: 19 - Linear DP

---
APPROACH: Binary search + prefix sums
- Given array and queries [cap_value, k], find the maximum sum of a
  subsequence of length k where each element is capped at cap_value.
- Sort elements. For each query, use binary search to find how many
  elements exceed cap. Use prefix sums for fast range sum.
- Take the k largest elements after capping.

Time: O(n log n + q * log n)  Space: O(n)
---
"""

from typing import List
import bisect


class Solution:
    def maxSubsequenceSum(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sorted_nums = sorted(nums, reverse=True)
        n = len(sorted_nums)

        # Prefix sums of sorted (descending) array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + sorted_nums[i]

        # Sorted ascending for binary search
        asc = sorted(nums)
        prefix_asc = [0] * (n + 1)
        for i in range(n):
            prefix_asc[i + 1] = prefix_asc[i] + asc[i]

        results = []
        for cap, k in queries:
            # Take k largest elements, each capped at cap.
            # Among top k elements (sorted_nums[0..k-1]):
            # Those > cap get capped to cap.
            # pos = number of top-k elements that are <= cap
            # Elements > cap in top-k: sorted descending, find first <= cap

            top_k = sorted_nums[:k]
            # In top_k (descending), find how many > cap
            # Using bisect on ascending sorted array:
            # Number of elements > cap total
            idx = bisect.bisect_right(asc, cap)  # asc[idx:] are > cap
            count_above = n - idx  # total elements > cap

            if count_above >= k:
                # All top k are > cap, sum = k * cap
                results.append(k * cap)
            else:
                # count_above elements capped, rest kept as is
                # Sum of top k elements not exceeding cap:
                # Top k sorted desc: first count_above might be > cap
                # Actually need to be more careful.
                # Sum of top k = prefix[k]
                # Among top k, how many exceed cap?
                # sorted_nums is descending: find first index where sorted_nums[i] <= cap
                lo, hi = 0, k
                while lo < hi:
                    mid = (lo + hi) // 2
                    if sorted_nums[mid] > cap:
                        lo = mid + 1
                    else:
                        hi = mid
                # lo = number of top-k elements > cap
                above_in_k = lo
                sum_below = prefix[k] - prefix[above_in_k]
                results.append(above_in_k * cap + sum_below)

        return results


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # [5,3,1,4,2], cap=3, k=3: top 3 = [5,4,3] -> capped [3,3,3] = 9
    res = sol.maxSubsequenceSum([5, 3, 1, 4, 2], [[3, 3]])
    assert res == [9], f"Got {res}"

    # No capping needed
    res = sol.maxSubsequenceSum([1, 2, 3], [[10, 2]])
    assert res == [5], f"Got {res}"

    print("All tests passed!")
