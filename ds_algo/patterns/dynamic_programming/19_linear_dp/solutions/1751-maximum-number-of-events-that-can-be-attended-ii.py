"""
1751. Maximum Number of Events That Can Be Attended II
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

Pattern: 19 - Linear DP

---
APPROACH: Sort by end time, DP with binary search
- Sort events by end time.
- dp[i][j] = max value attending from first i events choosing at most j events.
- For event i: either skip it, or attend it + best from events ending before start[i].
- Use binary search to find the latest event ending before start[i].

Time: O(n * k * log n)
Space: O(n * k)
---
"""

from typing import List
import bisect


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        ends = [e[1] for e in events]

        # dp[i][j] = max value from first i events, attending at most j
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start_i, end_i, val_i = events[i - 1]
            # Find latest event ending before start_i
            # We need end < start_i
            idx = bisect.bisect_left(ends, start_i, 0, i - 1)
            # idx is the first position where ends[pos] >= start_i
            # So the latest event ending before start_i is at idx - 1
            prev = idx  # number of events we can consider (0-indexed -> 1-indexed = idx)

            for j in range(1, k + 1):
                # Skip event i
                dp[i][j] = dp[i - 1][j]
                # Attend event i
                dp[i][j] = max(dp[i][j], dp[prev][j - 1] + val_i)

        return dp[n][k]


# --- Tests ---
def test():
    sol = Solution()

    assert sol.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2) == 7
    assert sol.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2) == 10  # [2,3,10] alone beats any pair
    assert sol.maxValue([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3) == 9

    # Single event
    assert sol.maxValue([[1, 5, 10]], 1) == 10

    # k = 1
    assert sol.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 1) == 4

    print("All tests passed!")


if __name__ == "__main__":
    test()
