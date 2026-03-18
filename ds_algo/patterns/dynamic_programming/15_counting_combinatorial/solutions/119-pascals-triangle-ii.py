"""
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Pattern: 15 - Counting/Combinatorial DP

---
APPROACH: Single row, update in-place right to left
- Only need one row at a time → O(rowIndex) space
- Update right to left so row[j-1] isn't overwritten before use
  (same trick as 0/1 knapsack and #115)

Time: O(rowIndex^2)  Space: O(rowIndex)
---
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]

        return row


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.getRow(3) == [1, 3, 3, 1]
    assert sol.getRow(0) == [1]
    assert sol.getRow(1) == [1, 1]
    assert sol.getRow(4) == [1, 4, 6, 4, 1]

    print("all tests passed")
