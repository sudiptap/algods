"""
1000. Minimum Cost to Merge Stones (Hard)

Pattern: 07_matrix_chain_multiplication
- Interval DP generalizing matrix chain multiplication to k-way merges.

Approach:
- We can only merge k consecutive piles into one. A range [i..j] can be fully
  merged into 1 pile only if (j - i) % (k - 1) == 0.
- dp[i][j] = minimum cost to optimally merge stones[i..j] (as far as possible).
- Transition: split at every point m where [i..m] can reduce to 1 pile,
  i.e., m steps from i by (k-1): dp[i][j] = min(dp[i][m] + dp[m+1][j]).
- After splitting, if (j - i) % (k - 1) == 0, we can do one final merge
  of the whole range, adding prefix_sum[j+1] - prefix_sum[i].
- If it's impossible to merge all into 1 pile, return -1.

Complexity:
- Time:  O(n^3 / k) due to step size k-1 in splits
- Space: O(n^2)
"""

from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if n == 1:
            return 0
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        INF = float('inf')
        dp = [[0] * n for _ in range(n)]

        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = INF
                for m in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])
                if (j - i) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]

        return dp[0][n - 1]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: stones=[3,2,4,1], k=2 -> 20
    assert sol.mergeStones([3, 2, 4, 1], 2) == 20

    # Example 2: stones=[3,2,4,1], k=3 -> impossible
    assert sol.mergeStones([3, 2, 4, 1], 3) == -1

    # Example 3: stones=[3,5,1,2,6], k=3 -> 25
    assert sol.mergeStones([3, 5, 1, 2, 6], 3) == 25

    # Single stone
    assert sol.mergeStones([5], 2) == 0

    # Two stones, k=2
    assert sol.mergeStones([1, 2], 2) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
