"""
85. Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/

Pattern: 10 - DP on Grids (also: Monotonic Stack)

---
APPROACH 1: Heights + Largest Rectangle in Histogram (optimal)
- Build a histogram of heights for each row:
    heights[j] = (heights[j] + 1) if matrix[i][j] == '1' else 0
- For each row, solve "Largest Rectangle in Histogram" (#84) using monotonic stack
- This reduces a 2D problem to n * 1D problems

Time: O(rows * cols)  Space: O(cols)

APPROACH 2: DP with height/left/right arrays
- For each cell, track:
    height[j]: consecutive 1s above (including current)
    left[j]:   leftmost column where this height starts
    right[j]:  rightmost column where this height ends (exclusive)
- Area at (i,j) = height[j] * (right[j] - left[j])

Time: O(rows * cols)  Space: O(cols)
---
"""

from typing import List


# ---------- Approach 1: Heights + Monotonic Stack ----------
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # update histogram heights
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0

            # largest rectangle in histogram using monotonic stack
            max_area = max(max_area, self._largestRectangleArea(heights))

        return max_area

    def _largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # indices of increasing heights
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            h = heights[i] if i < n else 0
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area


# ---------- Approach 2: DP with left/right boundaries ----------
class SolutionDP:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        height = [0] * cols
        left = [0] * cols        # leftmost valid column for current height
        right = [cols] * cols    # rightmost valid column (exclusive)
        max_area = 0

        for i in range(rows):
            # update heights
            for j in range(cols):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            # update left boundaries (scan left to right)
            cur_left = 0
            for j in range(cols):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            # update right boundaries (scan right to left)
            cur_right = cols
            for j in range(cols - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = cols
                    cur_right = j

            # compute area
            for j in range(cols):
                max_area = max(max_area, height[j] * (right[j] - left[j]))

        return max_area


# ---------- Tests ----------
if __name__ == "__main__":
    for Sol in [Solution, SolutionDP]:
        sol = Sol()

        assert sol.maximalRectangle([
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]) == 6

        assert sol.maximalRectangle([["0"]]) == 0
        assert sol.maximalRectangle([["1"]]) == 1
        assert sol.maximalRectangle([]) == 0

        assert sol.maximalRectangle([
            ["1", "1"],
            ["1", "1"]
        ]) == 4

        print(f"{Sol.__name__}: all tests passed")
