"""
3801. Minimum Cost to Merge Sorted Lists
https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

Pattern: 07 - Matrix Chain Multiplication (Interval DP)

---
APPROACH: Bitmask DP on which lists have been merged
- n <= 12 lists, so use bitmask DP.
- State: dp[mask] = dict mapping (length, median_index) to min cost.
  Actually, after merging a subset, the result is a sorted list whose
  elements are the union of all elements in the subset.
- Precompute for each subset: the merged sorted list's length and median.
- dp[mask] = min cost to merge all lists in mask into one.
- Transition: split mask into two non-empty subsets, merge the results.

Time: O(3^n * n)  Space: O(2^n)
---
"""

from typing import List


class Solution:
    def minimumCost(self, lists: List[List[int]]) -> int:
        n = len(lists)
        if n == 1:
            return 0

        # Precompute for each bitmask: the sorted merged list
        # Since total elements <= 2000, this is feasible.
        full = 1 << n

        # For each singleton mask, store the sorted list
        merged = [None] * full
        for i in range(n):
            merged[1 << i] = lists[i][:]

        # Precompute merged lists for all masks (using subset combination)
        # Actually we don't need all merged lists, just length and median.
        # Precompute length and median for each mask.

        import bisect

        # Length of merged list for mask
        mask_len = [0] * full
        mask_median = [0] * full  # median value

        # Build sorted merged lists for all masks
        # This could be expensive for large masks. Total elements <= 2000.
        # Use a different approach: just precompute length and median.
        # The merged sorted list for a mask is the sorted union of all elements.

        # Precompute all elements for each mask
        # For small n (<=12), iterate over subsets.
        all_elements = [[] for _ in range(full)]
        for i in range(n):
            all_elements[1 << i] = lists[i][:]

        for mask in range(1, full):
            if mask & (mask - 1) == 0:
                # singleton, already set
                pass
            else:
                # Find lowest set bit and combine
                low = mask & (-mask)
                rest = mask ^ low
                # Merge sorted lists
                a = all_elements[low]
                b = all_elements[rest]
                merged_list = []
                i, j = 0, 0
                while i < len(a) and j < len(b):
                    if a[i] <= b[j]:
                        merged_list.append(a[i])
                        i += 1
                    else:
                        merged_list.append(b[j])
                        j += 1
                merged_list.extend(a[i:])
                merged_list.extend(b[j:])
                all_elements[mask] = merged_list

            L = len(all_elements[mask])
            mask_len[mask] = L
            # Median: middle element, or left-middle for even length
            mask_median[mask] = all_elements[mask][(L - 1) // 2] if L > 0 else 0

        # DP: dp[mask] = min cost to merge all lists in mask into one list
        dp = [float('inf')] * full
        for i in range(n):
            dp[1 << i] = 0

        for mask in range(1, full):
            if bin(mask).count('1') <= 1:
                continue
            # Try all ways to split mask into two non-empty subsets
            sub = (mask - 1) & mask
            while sub > 0:
                comp = mask ^ sub
                if sub < comp:  # avoid double counting
                    cost = dp[sub] + dp[comp]
                    # Cost to merge the two resulting lists
                    merge_cost = mask_len[sub] + mask_len[comp] + abs(mask_median[sub] - mask_median[comp])
                    dp[mask] = min(dp[mask], cost + merge_cost)
                sub = (sub - 1) & mask

        return dp[full - 1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumCost([[1, 3, 5], [2, 4], [6, 7, 8]]) == 18
    assert sol.minimumCost([[1, 1, 5], [1, 4, 7, 8]]) == 10
    assert sol.minimumCost([[1], [3]]) == 4
    assert sol.minimumCost([[1], [1]]) == 2

    print("all tests passed")
