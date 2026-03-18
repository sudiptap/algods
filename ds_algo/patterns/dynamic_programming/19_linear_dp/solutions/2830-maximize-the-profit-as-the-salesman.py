"""
2830. Maximize the Profit as the Salesman
https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

Pattern: 19 - Linear DP

---
APPROACH: Group offers by their end house. Sweep dp from 0..n-1.
- dp[i] = max profit considering houses 0..i.
- For each house i, either skip it (dp[i] = dp[i-1]) or sell a range
  ending at i: dp[i] = max(dp[i], dp[start-1] + gold).
- Grouping offers by end avoids binary search (similar to 2008).

Time: O(n + m) where m = number of offers  Space: O(n)
---
"""

from typing import List
from collections import defaultdict


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        """Return maximum gold from selling non-overlapping house ranges."""
        # Group offers by end house
        offers_at_end = defaultdict(list)
        for start, end, gold in offers:
            offers_at_end[end].append((start, gold))

        dp = [0] * (n + 1)
        # dp is 1-indexed offset: dp[i+1] = best profit for houses 0..i
        for i in range(n):
            dp[i + 1] = dp[i]  # skip house i
            for start, gold in offers_at_end[i]:
                dp[i + 1] = max(dp[i + 1], dp[start] + gold)

        return dp[n]


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.maximizeTheProfit(5, [[0, 0, 1], [0, 2, 2], [1, 3, 2]]) == 3

    # Example 2
    assert sol.maximizeTheProfit(
        5, [[0, 0, 1], [0, 2, 10], [1, 3, 2]]
    ) == 10

    # Single offer
    assert sol.maximizeTheProfit(3, [[0, 2, 5]]) == 5

    # No offers
    assert sol.maximizeTheProfit(5, []) == 0

    # Non-overlapping offers
    assert sol.maximizeTheProfit(
        6, [[0, 1, 3], [2, 3, 4], [4, 5, 5]]
    ) == 12

    # All overlapping, pick best
    assert sol.maximizeTheProfit(
        3, [[0, 2, 5], [0, 2, 10], [0, 2, 3]]
    ) == 10

    print("All tests passed!")


if __name__ == "__main__":
    test()
