"""
2915. Length of the Longest Subsequence That Sums to Target
https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

Pattern: 02 - 0/1 Knapsack

---
APPROACH: Classic 0/1 knapsack maximizing count instead of value.
- dp[j] = maximum length of a subsequence that sums to exactly j.
- For each num, iterate j from target down to num (standard 0/1 trick).
- dp[j] = max(dp[j], dp[j - num] + 1).
- Return dp[target] if reachable, else -1.

Time: O(n * target)  Space: O(target)
---
"""

from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        """Return length of longest subsequence summing to target, or -1."""
        dp = [-1] * (target + 1)
        dp[0] = 0

        for num in nums:
            for j in range(target, num - 1, -1):
                if dp[j - num] != -1:
                    dp[j] = max(dp[j], dp[j - num] + 1)

        return dp[target]


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.lengthOfLongestSubsequence([1, 2, 3, 4, 5], 9) == 3

    # Example 2
    assert sol.lengthOfLongestSubsequence([4, 1, 3, 2, 1, 5], 7) == 4

    # Example 3 — impossible
    assert sol.lengthOfLongestSubsequence([1, 1, 5, 4, 5], 3) == -1

    # Single element equals target
    assert sol.lengthOfLongestSubsequence([5], 5) == 1

    # Single element doesn't match
    assert sol.lengthOfLongestSubsequence([3], 5) == -1

    # All ones
    assert sol.lengthOfLongestSubsequence([1, 1, 1, 1], 3) == 3

    # Target is 0 — empty subsequence not valid per constraints (target >= 1)
    # but dp[0]=0 means length 0 which is correct edge

    print("All tests passed!")


if __name__ == "__main__":
    test()
