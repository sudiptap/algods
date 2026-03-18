"""
2008. Maximum Earnings From Taxi
https://leetcode.com/problems/maximum-earnings-from-taxi/

Pattern: 19 - Linear DP

---
APPROACH: Group rides by their end point. Sweep dp from 1..n.
- dp[i] = maximum earnings considering points 1..i.
- For each point i, either skip it (dp[i] = dp[i-1]) or take a ride
  ending at i: dp[i] = max(dp[i], dp[start] + (end - start + tip)).
- Grouping rides by end avoids binary search entirely.

Time: O(n + m) where m = number of rides  Space: O(n)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        """Return maximum earnings from picking up non-overlapping taxi rides."""
        # Group rides by their end point
        rides_at_end = defaultdict(list)
        for start, end, tip in rides:
            rides_at_end[end].append((start, end - start + tip))

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]  # skip point i
            for start, earning in rides_at_end[i]:
                dp[i] = max(dp[i], dp[start] + earning)

        return dp[n]


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.maxTaxiEarnings(5, [[2, 5, 4], [1, 5, 1]]) == 7

    # Example 2
    assert sol.maxTaxiEarnings(
        20,
        [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2],
         [12, 15, 2], [13, 18, 1]]
    ) == 20

    # Single ride
    assert sol.maxTaxiEarnings(5, [[1, 5, 3]]) == 7

    # No rides
    assert sol.maxTaxiEarnings(5, []) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test()
