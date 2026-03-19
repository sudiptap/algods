"""
1230. Toss Strange Coins (Medium)

Pattern: 17_probability_dp
- Probability of getting exactly target heads from n coins with different probabilities.

Approach:
- dp[i][j] = probability of getting exactly j heads after tossing the first i coins.
- Base: dp[0][0] = 1.0.
- Transition: dp[i][j] = dp[i-1][j-1] * prob[i-1] + dp[i-1][j] * (1 - prob[i-1]).
- Answer: dp[n][target].
- Space optimization: use 1D array, iterate j in reverse.

Complexity:
- Time:  O(n * target)
- Space: O(target)
"""

from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [0.0] * (target + 1)
        dp[0] = 1.0

        for i in range(n):
            p = prob[i]
            for j in range(min(i + 1, target), 0, -1):
                dp[j] = dp[j] * (1 - p) + dp[j - 1] * p
            dp[0] *= (1 - p)

        return dp[target]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    result = sol.probabilityOfHeads([0.4], 1)
    assert abs(result - 0.4) < 1e-5

    # Example 2
    result = sol.probabilityOfHeads([0.5, 0.5, 0.5, 0.5, 0.5], 0)
    assert abs(result - 0.03125) < 1e-5

    # All heads certain
    result = sol.probabilityOfHeads([1.0, 1.0], 2)
    assert abs(result - 1.0) < 1e-5

    # Impossible target
    result = sol.probabilityOfHeads([0.0, 0.0], 1)
    assert abs(result - 0.0) < 1e-5

    # Fair coins, 2 heads out of 3
    result = sol.probabilityOfHeads([0.5, 0.5, 0.5], 2)
    assert abs(result - 0.375) < 1e-5

    print("All tests passed!")


if __name__ == "__main__":
    test()
