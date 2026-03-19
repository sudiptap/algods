"""
1531. String Compression II
https://leetcode.com/problems/string-compression-ii/

Pattern: 16 - String DP

---
APPROACH: DP on string with deletions
- dp[i][k] = minimum length of run-length encoding of s[:i] using at most k deletions
- For each position i, either delete s[i] (use one deletion) or keep it
- When keeping s[i], try extending a run by skipping different characters
- Key insight: for each position, try keeping a run of same characters by
  deleting non-matching ones in between

Time: O(n^2 * k) where n = len(s)
Space: O(n * k)
---
"""

from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        def encoded_len(count):
            if count == 0:
                return 0
            if count == 1:
                return 1
            if count < 10:
                return 2
            if count < 100:
                return 3
            return 4

        @lru_cache(maxsize=None)
        def dp(i, k):
            if k < 0:
                return float('inf')
            if i >= n:
                return 0
            # Option 1: delete s[i]
            res = dp(i + 1, k - 1)
            # Option 2: keep s[i], start a run from here
            # Count how many same chars we can keep by deleting others
            deletes = 0
            count = 0
            for j in range(i, n):
                if s[j] == s[i]:
                    count += 1
                else:
                    deletes += 1
                if deletes > k:
                    break
                # Keep s[i..j] with deletes non-matching chars removed
                res = min(res, encoded_len(count) + dp(j + 1, k - deletes))
            return res

        return dp(0, k)


# --- Tests ---
def test():
    sol = Solution()

    # Example 1
    assert sol.getLengthOfOptimalCompression("aaabcccd", 2) == 4  # "a3c3" or "a3d" -> "a3c3" is len 4

    # Example 2
    assert sol.getLengthOfOptimalCompression("aabbaa", 2) == 2  # delete bb -> "a4" len 2

    # Example 3
    assert sol.getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3  # "a11" len 3

    # Single char
    assert sol.getLengthOfOptimalCompression("a", 0) == 1
    assert sol.getLengthOfOptimalCompression("a", 1) == 0

    # All same
    assert sol.getLengthOfOptimalCompression("aaa", 0) == 2  # "a3"

    print("All tests passed!")


if __name__ == "__main__":
    test()
