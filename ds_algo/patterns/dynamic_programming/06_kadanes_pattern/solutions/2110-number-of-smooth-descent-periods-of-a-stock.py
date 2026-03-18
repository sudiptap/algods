"""
2110. Number of Smooth Descent Periods of a Stock
https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

Pattern: 06 - Kadane's Pattern

---
APPROACH: Track the current streak of smooth descent.
- A smooth descent period has prices[i] - prices[i+1] == 1.
- If prices[i] - prices[i-1] == -1 (i.e. decreased by 1), extend streak.
- Otherwise reset streak to 1.
- Each day with streak length k contributes k new smooth descent periods
  (the k substrings ending at that day).

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        """Return total number of smooth descent periods."""
        total = 1
        streak = 1

        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                streak += 1
            else:
                streak = 1
            total += streak

        return total


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.getDescentPeriods([3, 2, 1, 4]) == 7

    # Example 2
    assert sol.getDescentPeriods([8, 6, 7, 7]) == 4

    # Example 3: single element
    assert sol.getDescentPeriods([1]) == 1

    # Long descent
    assert sol.getDescentPeriods([5, 4, 3, 2, 1]) == 15  # 5+4+3+2+1

    # All same
    assert sol.getDescentPeriods([3, 3, 3]) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
