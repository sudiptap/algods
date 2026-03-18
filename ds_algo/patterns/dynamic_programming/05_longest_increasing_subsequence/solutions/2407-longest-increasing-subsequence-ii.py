"""
2407. Longest Increasing Subsequence II
https://leetcode.com/problems/longest-increasing-subsequence-ii/

Pattern: 05 - Longest Increasing Subsequence

---
APPROACH: Segment tree for range max query.
dp[v] = length of LIS ending with value v.
For each nums[i], query max of dp[nums[i]-k .. nums[i]-1], set dp[nums[i]] = max+1.
A segment tree supports both operations in O(log max_val).

Time: O(n * log(max_val))  Space: O(max_val)
---
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        """Return the length of the longest strictly increasing subsequence
        where the difference between adjacent elements is at most k."""
        max_val = max(nums)
        tree = [0] * (4 * (max_val + 1))

        def update(node: int, lo: int, hi: int, pos: int, val: int) -> None:
            if lo == hi:
                tree[node] = val
                return
            mid = (lo + hi) // 2
            if pos <= mid:
                update(2 * node, lo, mid, pos, val)
            else:
                update(2 * node + 1, mid + 1, hi, pos, val)
            tree[node] = max(tree[2 * node], tree[2 * node + 1])

        def query(node: int, lo: int, hi: int, ql: int, qr: int) -> int:
            if ql > qr or lo > qr or hi < ql:
                return 0
            if ql <= lo and hi <= qr:
                return tree[node]
            mid = (lo + hi) // 2
            return max(
                query(2 * node, lo, mid, ql, qr),
                query(2 * node + 1, mid + 1, hi, ql, qr),
            )

        ans = 0
        for v in nums:
            left = max(1, v - k)
            right = v - 1
            best = query(1, 1, max_val, left, right) if right >= left else 0
            cur = best + 1
            if cur > ans:
                ans = cur
            update(1, 1, max_val, v, cur)

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: [4,2,1,4,3,4,5,8,15], k=3 -> 5 ([1,3,4,5,8])
    assert sol.lengthOfLIS([4, 2, 1, 4, 3, 4, 5, 8, 15], 3) == 5
    # Example 2: [7,4,5,1,8,12,4,7], k=5 -> 4 ([4,5,8,12])
    assert sol.lengthOfLIS([7, 4, 5, 1, 8, 12, 4, 7], 5) == 4
    # Example 3: [1,5], k=1 -> 1 (diff=4 > k=1)
    assert sol.lengthOfLIS([1, 5], 1) == 1
    # Single element
    assert sol.lengthOfLIS([10], 5) == 1
    # Strictly increasing within k
    assert sol.lengthOfLIS([1, 2, 3, 4, 5], 1) == 5

    print("all tests passed")
