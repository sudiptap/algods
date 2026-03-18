"""
1639. Number of Ways to Form a Target String Given a Dictionary (Hard)
https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

Given a list of strings `words` (all same length) and a string `target`,
return the number of ways to form `target` using the following rules:
- `target` is formed from left to right.
- To form the i-th character of target, pick the k-th character from one of
  the strings in `words` (each string character can be used at most once per
  formation).
- Once you use the k-th character of any string, you can no longer use the
  x-th character of any string where x <= k.
- Return answer modulo 10^9 + 7.

Approach:
    1. Precompute freq[k][c] = how many words have character c at column k.
    2. dp[j][k] = number of ways to form target[:j] using only columns[:k].
       - Skip column k: dp[j][k] = dp[j][k-1]
       - Use column k for target[j-1]: dp[j][k] = dp[j-1][k-1] * freq[k][target[j-1]]
    3. Optimize to 1-D by iterating j in reverse for each column k.

Time:  O(m * n + m * t) where m = len(words[0]), n = len(words), t = len(target)
Space: O(t + 26*m) for dp array and frequency table
"""

from typing import List
from collections import defaultdict


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """Return the number of ways to form target from dictionary columns.

        Precompute character frequencies per column, then use 1-D DP.

        Args:
            words: List of strings, all same length.
            target: Target string to form.

        Returns:
            Number of ways modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        m = len(words[0])  # number of columns
        t = len(target)

        # freq[k][c] = count of character c at column k
        freq = [defaultdict(int) for _ in range(m)]
        for word in words:
            for k, ch in enumerate(word):
                freq[k][ch] += 1

        # dp[j] = ways to form target[:j]
        dp = [0] * (t + 1)
        dp[0] = 1  # empty target: one way

        for k in range(m):
            # Iterate j in reverse to avoid using same column twice
            for j in range(min(t, k + 1), 0, -1):
                c = target[j - 1]
                if c in freq[k]:
                    dp[j] = (dp[j] + dp[j - 1] * freq[k][c]) % MOD

        return dp[t]


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.numWays(["acca", "bbbb", "caca"], "aba") == 6

    # Example 2
    assert sol.numWays(["abba", "baab"], "bab") == 4

    # Target longer than word length => impossible
    assert sol.numWays(["ab", "cd"], "abc") == 0

    # Single character target
    assert sol.numWays(["abc", "abc"], "a") == 2

    # Target equals one word exactly
    assert sol.numWays(["abc"], "abc") == 1

    print("All tests passed!")
