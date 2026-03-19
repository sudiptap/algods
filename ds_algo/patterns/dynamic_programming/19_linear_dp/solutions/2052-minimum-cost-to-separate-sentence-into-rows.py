"""
2052. Minimum Cost to Separate Sentence Into Rows (Medium)
https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

Given a sentence of words and max row length k, split into rows. Cost of
a row (except last) = (k - row_length)^2. Minimize total cost.

Pattern: Linear DP
Approach:
- dp[i] = minimum cost to fit words[i:] into rows.
- For each i, try placing words[i..j] on one row if total length
  (including spaces) <= k.
- If j == n-1 (last word on this row is the final word), cost = 0 for
  this row.
- Otherwise, cost = (k - length)^3.
- dp[i] = min over valid j of (cost(i,j) + dp[j+1]).

Time:  O(n * k) where n = number of words
Space: O(n)
"""


class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        """Return minimum cost to split sentence into rows of at most k chars.

        Args:
            sentence: Space-separated words.
            k: Maximum characters per row.

        Returns:
            Minimum total cost.
        """
        words = sentence.split()
        n = len(words)
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            length = 0
            for j in range(i, n):
                length += len(words[j])
                if j > i:
                    length += 1  # space
                if length > k:
                    break
                if j == n - 1:
                    cost = 0  # last row is free
                else:
                    cost = (k - length) ** 2
                dp[i] = min(dp[i], cost + dp[j + 1])

        return dp[0]


# ---------- tests ----------
def test_minimum_cost():
    sol = Solution()

    # Example 1
    assert sol.minimumCost("i love leetcode", 12) == 36

    # Example 2
    assert sol.minimumCost("apples and bananas taste great", 7) == 21

    # Example 3
    assert sol.minimumCost("a", 5) == 0

    # Single word fits exactly
    assert sol.minimumCost("hello", 5) == 0

    # All on one row
    assert sol.minimumCost("a b c", 5) == 0

    print("All tests passed for 2052. Minimum Cost to Separate Sentence Into Rows")


if __name__ == "__main__":
    test_minimum_cost()
