"""
1955. Count Number of Special Subsequences (Hard)
https://leetcode.com/problems/count-number-of-special-subsequences/

A special subsequence consists of positive number of 0s, then positive
number of 1s, then positive number of 2s. Count such subsequences mod 10^9+7.

Pattern: State Machine DP
Approach:
- Three states tracking count of subsequences:
  - a = subsequences consisting of only 0s
  - b = subsequences consisting of 0s followed by 1s
  - c = subsequences consisting of 0s, 1s, then 2s (complete)
- For each element:
  - If 0: a = 2*a + 1 (extend each existing 0-seq or start new)
  - If 1: b = 2*b + a (extend each existing 01-seq or append 1 to any 0-seq)
  - If 2: c = 2*c + b (extend each existing 012-seq or append 2 to any 01-seq)

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        """Return count of special subsequences mod 10^9+7.

        Args:
            nums: Array of 0s, 1s, and 2s.

        Returns:
            Number of special subsequences.
        """
        MOD = 10**9 + 7
        a = b = c = 0

        for x in nums:
            if x == 0:
                a = (2 * a + 1) % MOD
            elif x == 1:
                b = (2 * b + a) % MOD
            else:
                c = (2 * c + b) % MOD

        return c


# ---------- tests ----------
def test_special_subsequences():
    sol = Solution()

    # Example 1: [0,1,2,2] -> 3
    assert sol.countSpecialSubsequences([0, 1, 2, 2]) == 3

    # Example 2: [2,2,0,0] -> 0
    assert sol.countSpecialSubsequences([2, 2, 0, 0]) == 0

    # Example 3: [0,1,2,0,1,2] -> 7
    assert sol.countSpecialSubsequences([0, 1, 2, 0, 1, 2]) == 7

    # Minimal: [0,1,2] -> 1
    assert sol.countSpecialSubsequences([0, 1, 2]) == 1

    # No 2s
    assert sol.countSpecialSubsequences([0, 1, 0, 1]) == 0

    print("All tests passed for 1955. Count Number of Special Subsequences")


if __name__ == "__main__":
    test_special_subsequences()
