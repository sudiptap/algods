"""
873. Length of Longest Fibonacci-Like Subsequence (Medium)
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

Given a strictly increasing array arr, find the length of the longest
Fibonacci-like subsequence. A sequence x1, x2, ..., xn is Fibonacci-like if
n >= 3 and xi + xi+1 = xi+2 for all i.

Pattern: Longest Increasing Subsequence variant
Approach:
- dp[i][j] = length of Fibonacci subsequence ending with arr[i], arr[j] (i < j).
- For each pair (i, j), look for arr[k] = arr[j] - arr[i] where k < i.
  Use a hashmap val_to_idx for O(1) lookup.
- dp[i][j] = dp[k][i] + 1 if k exists, else 2 (just the pair).
- Answer: max over all dp[i][j] if >= 3, else 0.

Time:  O(n^2) — iterate all pairs (i, j).
Space: O(n^2) — for dp table (can use dict to be sparse).
"""

from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """Return length of longest Fibonacci-like subsequence.

        Args:
            arr: Strictly increasing array, len >= 3.

        Returns:
            Length of longest Fibonacci-like subsequence, or 0 if none.
        """
        n = len(arr)
        idx = {v: i for i, v in enumerate(arr)}
        dp = {}
        ans = 0

        for j in range(n):
            for i in range(j):
                prev_val = arr[j] - arr[i]
                # prev_val must be < arr[i] for strictly increasing
                if prev_val < arr[i] and prev_val in idx:
                    k = idx[prev_val]
                    dp[i, j] = dp.get((k, i), 2) + 1
                    ans = max(ans, dp[i, j])

        return ans if ans >= 3 else 0


# ---------- tests ----------
def test_len_longest_fib_subseq():
    sol = Solution()

    # Example 1: [1,2,3,4,5,6,7,8] -> [1,2,3,5,8] length 5
    assert sol.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]) == 5

    # Example 2: [1,3,7,11,12,14,18] -> [1,11,12] or [3,11,14] or [7,11,18] length 3
    assert sol.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]) == 3

    # No fibonacci subsequence
    assert sol.lenLongestFibSubseq([1, 2, 4, 8, 16]) == 0

    # Minimal fibonacci: [1, 2, 3]
    assert sol.lenLongestFibSubseq([1, 2, 3]) == 3

    # [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]
    # 4,14,18,32,50 -> 4+14=18, 14+18=32, 18+32=50 -> length 5
    assert sol.lenLongestFibSubseq([2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]) == 5

    print("All tests passed for 873. Length of Longest Fibonacci Subsequence")


if __name__ == "__main__":
    test_len_longest_fib_subseq()
