"""
2355. Maximum Number of Books You Can Take
https://leetcode.com/problems/maximum-number-of-books-you-can-take/

Pattern: 19 - Linear DP

---
APPROACH: Monotonic stack
- For a contiguous section ending at index i, we take books[i] from shelf i,
  books[i]-1 from shelf i-1, ..., but cannot exceed books[j] for shelf j.
- dp[i] = max books from a contiguous section ending at i.
- Use monotonic stack: if books[i] - i is non-decreasing, extend previous.
  Otherwise, the section is limited by how far back we can go.
- When books[j] - j <= books[i] - i, we can extend from dp[j].
- Arithmetic sum for the "constrained" part.

Time: O(n)  Space: O(n)
---
"""

from typing import List


class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        dp = [0] * n
        stack = []  # stores indices, monotonic on books[i] - i

        def arith_sum(end_val, count):
            """Sum of end_val, end_val-1, ..., end_val-count+1, but each >= 0."""
            # If end_val - count + 1 < 0, some terms are 0
            start_val = max(0, end_val - count + 1)
            actual_count = end_val - start_val + 1
            return actual_count * (start_val + end_val) // 2

        for i in range(n):
            # Pop stack while books[stack[-1]] - stack[-1] >= books[i] - i
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()

            if stack:
                j = stack[-1]
                # From j+1 to i, we take books[i], books[i]-1, ..., books[i]-(i-j-1)
                count = i - j
                dp[i] = dp[j] + arith_sum(books[i], count)
            else:
                # From 0 to i
                count = i + 1
                dp[i] = arith_sum(books[i], count)

            stack.append(i)

        return max(dp)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumBooks([8, 5, 2, 7, 9]) == 19
    assert sol.maximumBooks([7, 0, 3, 4, 5]) == 12
    assert sol.maximumBooks([8, 2, 3, 7, 3, 4, 0, 1, 4, 3]) == 13
    assert sol.maximumBooks([1]) == 1

    print("all tests passed")
