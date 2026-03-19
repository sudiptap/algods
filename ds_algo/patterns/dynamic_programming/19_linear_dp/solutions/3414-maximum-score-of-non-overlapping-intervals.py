"""
3414. Maximum Score of Non-overlapping Intervals
https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

Pattern: 19 - Linear DP (Sort + DP + Binary Search)

---
APPROACH: Sort intervals by end time. dp[i][j] = max score picking j intervals from first i.
- Binary search for last non-overlapping interval.
- Pick at most 4 intervals. Track indices for reconstruction.

Time: O(n log n)  Space: O(n)
---
"""

from typing import List
import bisect


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Attach original index, sort by end
        indexed = sorted(enumerate(intervals), key=lambda x: x[1][1])
        ends = [intervals[idx][1] for idx, _ in indexed]

        # For interval i (sorted), find latest j where end[j] < start[i]
        def find_prev(i):
            start_i = indexed[i][1][0]
            # Find rightmost end < start_i
            pos = bisect.bisect_left(ends, start_i) - 1
            return pos

        # dp[i][j] = (max_weight, sorted list of original indices) using first i+1 intervals, picking j
        # j from 1..4
        INF = float('-inf')

        # dp[j] for rolling: at each interval i, dp_new[j] = best picking j from first i+1
        # We need lexicographically smallest indices for ties.

        # dp[j] = (weight, sorted_indices) for best using j picks from intervals seen so far
        # None means not achievable
        dp = [None] * 5  # dp[0..4]
        dp[0] = (0, [])

        # Also keep "best dp up to i" for binary search lookups
        # best[i][j] = best (weight, indices) considering intervals 0..i, picking j
        best = [[None] * 5 for _ in range(n)]

        def better(a, b):
            """Return the better of two (weight, indices) tuples: higher weight, then lex smaller indices."""
            if a is None:
                return b
            if b is None:
                return a
            if a[0] > b[0]:
                return a
            if b[0] > a[0]:
                return b
            # Same weight: pick lexicographically smaller indices
            return a if a[1] <= b[1] else b

        for i in range(n):
            orig_idx = indexed[i][0]
            weight = indexed[i][1][2]
            p = find_prev(i)

            # New dp considering interval i
            new_dp = [x for x in dp]  # copy: don't pick interval i

            # Pick interval i as the j-th pick
            if p >= 0:
                prev_best = best[p]
            else:
                prev_best = [None] * 5
                prev_best[0] = (0, [])

            for j in range(1, 5):
                if prev_best[j - 1] is not None:
                    pw, pidx = prev_best[j - 1]
                    new_val = pw + weight
                    new_indices = sorted(pidx + [orig_idx])
                    candidate = (new_val, new_indices)
                    new_dp[j] = better(new_dp[j], candidate)

            dp = new_dp
            for j in range(5):
                best[i][j] = dp[j]

        # Find best among dp[1..4]
        result = None
        for j in range(1, 5):
            result = better(result, dp[j])

        return result[1]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumWeight([[1, 3, 2], [4, 5, 2], [1, 5, 5], [6, 9, 3], [6, 7, 1], [8, 9, 1]]) == [2, 3]
    assert sol.maximumWeight([[5, 8, 1], [6, 7, 7], [4, 7, 3], [9, 10, 6], [7, 8, 2], [11, 14, 3], [3, 5, 5]]) == [1, 3, 5, 6]

    print("Solution: all tests passed")
