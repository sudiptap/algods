"""
2916. Subarrays Distinct Element Sum of Squares II
https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

Pattern: 20 - Prefix/Suffix DP (Segment tree with lazy propagation)

---
APPROACH: For each right endpoint r, maintain for each left endpoint l the
distinct count d(l,r). When adding nums[r], d(l,r) increases by 1 for all
l where nums[r] hasn't appeared in [l,r-1], i.e., l <= prev_occurrence.
Sum of d(l,r)^2 = sum of (d(l,r-1)+1)^2 for affected l, and d(l,r-1)^2 otherwise.
Use segment tree tracking sum of d^2 and sum of d with range increment.

Time: O(n log n)  Space: O(n)
---
"""

from typing import List

MOD = 10**9 + 7


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # Segment tree with lazy propagation
        # Each node stores: sum_d (sum of d values), sum_d2 (sum of d^2), cnt (number of elements)
        # Lazy: pending increment to add to all d values in range

        size = 1
        while size < n:
            size *= 2

        sum_d = [0] * (2 * size)
        sum_d2 = [0] * (2 * size)
        cnt = [0] * (2 * size)
        lazy = [0] * (2 * size)

        for i in range(n):
            cnt[size + i] = 1
        for i in range(size - 1, 0, -1):
            cnt[i] = cnt[2 * i] + cnt[2 * i + 1]

        def push_down(node):
            if lazy[node] != 0:
                for child in [2 * node, 2 * node + 1]:
                    inc = lazy[node]
                    # sum_d2 += 2*inc*sum_d + inc^2*cnt
                    sum_d2[child] = (sum_d2[child] + 2 * inc % MOD * sum_d[child] % MOD + inc * inc % MOD * cnt[child]) % MOD
                    sum_d[child] = (sum_d[child] + inc * cnt[child]) % MOD
                    lazy[child] = (lazy[child] + inc) % MOD
                lazy[node] = 0

        def update(node, lo, hi, ql, qr, inc):
            if qr < lo or hi < ql:
                return
            if ql <= lo and hi <= qr:
                sum_d2[node] = (sum_d2[node] + 2 * inc % MOD * sum_d[node] % MOD + inc * inc % MOD * cnt[node]) % MOD
                sum_d[node] = (sum_d[node] + inc * cnt[node]) % MOD
                lazy[node] = (lazy[node] + inc) % MOD
                return
            push_down(node)
            mid = (lo + hi) // 2
            update(2 * node, lo, mid, ql, qr, inc)
            update(2 * node + 1, mid + 1, hi, ql, qr, inc)
            sum_d2[node] = (sum_d2[2 * node] + sum_d2[2 * node + 1]) % MOD
            sum_d[node] = (sum_d[2 * node] + sum_d[2 * node + 1]) % MOD

        def query_all():
            return sum_d2[1]

        last_seen = {}
        ans = 0

        for r in range(n):
            # For subarrays ending at r, d(l,r) increases by 1 for l in [prev+1, r]
            prev = last_seen.get(nums[r], -1)
            # Increment d for l in [prev+1, r] (0-indexed)
            update(1, 0, size - 1, prev + 1, r, 1)
            ans = (ans + query_all()) % MOD
            last_seen[nums[r]] = r

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.sumCounts([1, 2, 1]) == 15
    assert sol.sumCounts([2, 2]) == 3

    print("All tests passed!")
