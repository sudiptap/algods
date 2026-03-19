"""
1246. Palindrome Removal (Hard)

Pattern: 08_palindromic_subsequence
- Minimum number of moves to remove all elements from array, where each move
  removes a palindromic subarray.

Approach:
- Interval DP: dp[i][j] = minimum moves to remove arr[i..j].
- Base: dp[i][i] = 1 (single element needs 1 move).
- Transition:
  - dp[i][j] = dp[i+1][j] + 1  (remove arr[i] alone, but can be improved)
  - If arr[i] == arr[k] for some k in [i+1, j]: dp[i][j] = min(dp[i][j], dp[i+1][k] + dp[k+1][j])
    because arr[i] can be removed together with arr[k] in the same palindrome.
  - Special case: if arr[i] == arr[i+1], dp[i][i+1] = 1.

Complexity:
- Time:  O(n^3)
- Space: O(n^2)
"""

from typing import List


class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Worst case: remove arr[i] alone + solve rest
                dp[i][j] = dp[i + 1][j] + 1

                for k in range(i + 1, j + 1):
                    if arr[i] == arr[k]:
                        # arr[i] and arr[k] can be in same palindrome removal
                        # dp[i+1][k-1] handles the middle (if i+1 > k-1, it's 0)
                        left = dp[i + 1][k - 1] if i + 1 <= k - 1 else 0
                        # Removing arr[i..k] as a palindrome costs max(1, left)
                        cost = max(1, left)
                        right = dp[k + 1][j] if k + 1 <= j else 0
                        dp[i][j] = min(dp[i][j], cost + right)

        return dp[0][n - 1]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: [1,2] -> 2 moves (remove 1, remove 2)
    assert sol.minimumMoves([1, 2]) == 2

    # Example 2: [1,3,4,1,5] -> 3 moves
    assert sol.minimumMoves([1, 3, 4, 1, 5]) == 3

    # Already palindrome
    assert sol.minimumMoves([1, 2, 1]) == 1

    # Single element
    assert sol.minimumMoves([1]) == 1

    # All same
    assert sol.minimumMoves([2, 2, 2, 2]) == 1

    # Two different
    assert sol.minimumMoves([1, 2]) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test()
