"""
1745. Palindrome Partitioning IV
https://leetcode.com/problems/palindrome-partitioning-iv/

Pattern: 08 - Palindromic Subsequence

---
APPROACH: Precompute isPalin[i][j], then check all split points
- Precompute isPalin[i][j] = True if s[i..j] is a palindrome (Manacher's or DP).
- Try all pairs of split points (i, j) where 0 < i < j < n:
  Check isPalin[0][i-1] and isPalin[i][j-1] and isPalin[j][n-1].

Time: O(n^2) for precomputation + O(n^2) for checking splits
Space: O(n^2)
---
"""


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)

        # Precompute isPalin[i][j]
        is_palin = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_palin[i + 1][j - 1]):
                    is_palin[i][j] = True

        # Try all split points
        for i in range(1, n - 1):
            if not is_palin[0][i - 1]:
                continue
            for j in range(i + 1, n):
                if is_palin[i][j - 1] and is_palin[j][n - 1]:
                    return True

        return False


# --- Tests ---
def test():
    sol = Solution()

    assert sol.checkPartitioning("abcbdd") == True   # "a" + "bcb" + "dd"
    assert sol.checkPartitioning("bcbddxy") == False
    assert sol.checkPartitioning("aaa") == True       # "a" + "a" + "a"
    assert sol.checkPartitioning("aba") == True       # "a" + "b" + "a"
    assert sol.checkPartitioning("abcba") == True     # "a" + "bcb" + "a"

    print("All tests passed!")


if __name__ == "__main__":
    test()
