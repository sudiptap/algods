"""
2926. Maximum Balanced Subsequence Sum
https://leetcode.com/problems/maximum-balanced-subsequence-sum/

Pattern: 05 - LIS (BIT/Segment tree for range max query)

---
APPROACH: A balanced subsequence requires nums[i] - i <= nums[j] - j for
consecutive elements. Let a[i] = nums[i] - i. Problem reduces to: find
subsequence with non-decreasing a[i] values that maximizes sum of nums[i].
Use coordinate compression + BIT for range max query.

Time: O(n log n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        a = [nums[i] - i for i in range(n)]

        # Coordinate compression
        sorted_unique = sorted(set(a))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
        m = len(sorted_unique)

        # BIT for range max query (prefix max)
        tree = [float('-inf')] * (m + 2)

        def update(i, val):
            while i <= m:
                tree[i] = max(tree[i], val)
                i += i & (-i)

        def query(i):
            res = float('-inf')
            while i > 0:
                res = max(res, tree[i])
                i -= i & (-i)
            return res

        ans = float('-inf')
        for i in range(n):
            r = rank[a[i]]
            best = query(r)  # max dp for all j with a[j] <= a[i]
            dp_i = nums[i] if best == float('-inf') else max(nums[i], best + nums[i])
            ans = max(ans, dp_i)
            update(r, dp_i)

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maxBalancedSubsequenceSum([3, 3, 5, 6]) == 14
    assert sol.maxBalancedSubsequenceSum([5, -1, -3, 8]) == 13
    assert sol.maxBalancedSubsequenceSum([-2, -1]) == -1

    print("All tests passed!")
