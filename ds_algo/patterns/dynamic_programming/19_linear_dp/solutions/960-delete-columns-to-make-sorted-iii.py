"""
960. Delete Columns to Make Sorted III (Hard)
https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

Given an array of n strings of the same length, delete the minimum number of
columns so that each remaining row (reading left to right) is in non-decreasing
lexicographic order (i.e., each row's kept characters are sorted).

Pattern: Linear DP (LIS on columns)
Approach:
- Think of columns as elements. Find the longest increasing subsequence of
  columns where "increasing" means column j >= column i character-by-character
  across ALL rows.
- dp[j] = length of longest valid column subsequence ending at column j.
- For each j, check all i < j: if column i <= column j in all rows,
  dp[j] = max(dp[j], dp[i] + 1).
- Answer: total_columns - max(dp).

Time:  O(n * m^2) where n = number of strings, m = string length.
Space: O(m)
"""

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """Return minimum columns to delete for all rows to be sorted.

        Args:
            strs: Array of equal-length strings.

        Returns:
            Minimum number of columns to delete.
        """
        n = len(strs)
        m = len(strs[0])
        dp = [1] * m

        for j in range(1, m):
            for i in range(j):
                # Check if column i <= column j in all rows
                if all(strs[r][i] <= strs[r][j] for r in range(n)):
                    dp[j] = max(dp[j], dp[i] + 1)

        return m - max(dp)


# ---------- tests ----------
def test_min_deletion_size():
    sol = Solution()

    # Example 1: ["babca","bbazb"] -> delete columns 0,4 -> "abc","baz"? No.
    # Actually delete col 0 and col 4: remaining "abca"->"abc"? Let me trust expected: 3
    assert sol.minDeletionSize(["babca", "bbazb"]) == 3

    # Example 2: ["edcba"] -> need sorted row, LIS of "edcba" = 1, delete 4
    assert sol.minDeletionSize(["edcba"]) == 4

    # Example 3: ["ghi","def","abc"] -> each row already sorted, delete 0
    assert sol.minDeletionSize(["ghi", "def", "abc"]) == 0

    # Single column
    assert sol.minDeletionSize(["a", "b"]) == 0

    # Already sorted rows
    assert sol.minDeletionSize(["abc", "bcd"]) == 0

    print("All tests passed for 960. Delete Columns to Make Sorted III")


if __name__ == "__main__":
    test_min_deletion_size()
