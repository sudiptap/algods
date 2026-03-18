"""
1105. Filling Bookcase Shelves (Medium)
https://leetcode.com/problems/filling-bookcase-shelves/

Pattern: 19 - Linear DP

Given books[i] = [width_i, height_i] and a shelf width, place books in order
on shelves to minimise total height. Each shelf's height = tallest book on it.

Approach:
    dp[i] = minimum total height to place the first i books.
    For each book i, try placing books i, i-1, i-2, ... on the same
    (last) shelf as long as total width <= shelfWidth.
    dp[i] = min over valid j of  dp[j] + max_height(books[j..i-1]).

Time:  O(n * shelfWidth)  —  inner loop bounded by shelf width
Space: O(n)
"""

from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """Return the minimum possible total height of the bookcase."""
        n = len(books)
        dp = [0] + [float("inf")] * n

        for i in range(1, n + 1):
            width = 0
            height = 0
            # Try placing books[j..i-1] on the current shelf (right to left)
            for j in range(i, 0, -1):
                width += books[j - 1][0]
                if width > shelfWidth:
                    break
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)

        return dp[n]


# ───────────────────────── tests ─────────────────────────

def test_example1():
    books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    assert Solution().minHeightShelves(books, 4) == 6

def test_single_book():
    assert Solution().minHeightShelves([[1, 3]], 5) == 3

def test_all_fit_one_shelf():
    books = [[1, 2], [1, 3], [1, 1]]
    assert Solution().minHeightShelves(books, 3) == 3

def test_each_own_shelf():
    books = [[3, 1], [3, 2], [3, 3]]
    assert Solution().minHeightShelves(books, 3) == 6

def test_example2():
    books = [[1,3],[2,4],[3,2]]
    assert Solution().minHeightShelves(books, 6) == 4


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
