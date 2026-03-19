"""
3316. Find Maximum Removals From Source String (Medium)

Pattern: 16_string_dp
- Given source, pattern, and targetIndices, find max number of indices from
  targetIndices we can remove from source such that pattern is still a subsequence.

Approach:
- dp[i][j] = max removals possible considering source[0..i-1] matched to pattern[0..j-1].
- If source[i-1] is in targetIndices, we can choose to remove it (dp[i-1][j] + 1)
  or keep it. If kept and matches pattern[j-1], dp[i-1][j-1].
- If source[i-1] not in targetIndices, skip: dp[i-1][j], or match: dp[i-1][j-1].

Complexity:
- Time:  O(n * m) where n = len(source), m = len(pattern)
- Space: O(m) with space optimization
"""

from typing import List


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        n, m = len(source), len(pattern)
        removable = set(targetIndices)
        INF = float('-inf')

        # dp[j] = max removals for matching pattern[0..j-1]
        dp = [0] + [INF] * m

        for i in range(1, n + 1):
            bonus = 1 if (i - 1) in removable else 0
            for j in range(min(i, m), 0, -1):
                # Option 1: skip source[i-1] (remove if possible)
                res = dp[j] + bonus
                # Option 2: match source[i-1] with pattern[j-1]
                if source[i - 1] == pattern[j - 1] and dp[j - 1] != INF:
                    res = max(res, dp[j - 1])
                dp[j] = res
            dp[0] += bonus

        return dp[m]


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1
    assert sol.maxRemovals("abbaa", "aba", [0, 1, 2]) == 1

    # Example 2
    assert sol.maxRemovals("bcda", "d", [0, 3]) == 2

    # Example 3
    assert sol.maxRemovals("dda", "dda", [0, 1, 2]) == 0

    # Example 4
    assert sol.maxRemovals("yeyeykyber", "yeyber", [0, 1, 2, 3, 4, 6, 7]) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test()
