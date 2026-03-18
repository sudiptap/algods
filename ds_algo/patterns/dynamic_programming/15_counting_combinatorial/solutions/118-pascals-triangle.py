"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Pattern: 15 - Counting/Combinatorial DP

---
APPROACH: Build row by row
- Each row[j] = prev_row[j-1] + prev_row[j]
- First and last elements are always 1

Time: O(numRows^2)  Space: O(numRows^2) for output
---
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        return triangle


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert sol.generate(1) == [[1]]
    assert sol.generate(2) == [[1], [1, 1]]

    print("all tests passed")
