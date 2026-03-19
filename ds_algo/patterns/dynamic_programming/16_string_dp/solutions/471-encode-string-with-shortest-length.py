"""
471. Encode String with Shortest Length (Hard)
https://leetcode.com/problems/encode-string-with-shortest-length/

Pattern: String DP / Interval DP

Given a string s, encode it such that its encoded length is the shortest.
The encoding rule is: k[encoded_string], where encoded_string is repeated
exactly k times.

Approach:
    Interval DP: dp[i][j] = shortest encoding of s[i..j].
    For each substring s[i..j]:
    1. Try splitting at every mid point: dp[i][mid] + dp[mid+1][j].
    2. Try encoding s[i..j] as k[pattern]:
       - Find the repeating unit using the (s+s).find(s,1) trick.
       - If the unit length divides the substring length, encode as
         k[dp[i][i+unit-1]].
    Take the shortest result.

Time:  O(n^3)
Space: O(n^2)
"""


class Solution:
    def encode(self, s: str) -> str:
        """Return the shortest encoded string for s."""
        n = len(s)
        if n <= 4:
            return s

        dp = [[""] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                sub = s[i:j + 1]
                dp[i][j] = sub  # default: no encoding

                if length <= 4:
                    continue

                # Try k[pattern] encoding
                # Find smallest repeating unit using concatenation trick
                doubled = sub + sub
                idx = doubled.find(sub, 1)
                if idx < length:
                    unit_len = idx
                    k = length // unit_len
                    candidate = f"{k}[{dp[i][i + unit_len - 1]}]"
                    if len(candidate) < len(dp[i][j]):
                        dp[i][j] = candidate

                # Try splitting
                for mid in range(i, j):
                    candidate = dp[i][mid] + dp[mid + 1][j]
                    if len(candidate) < len(dp[i][j]):
                        dp[i][j] = candidate

        return dp[0][n - 1]


# ───────────────────────── tests ─────────────────────────

def test_example1():
    assert Solution().encode("aaa") == "aaa"

def test_example2():
    assert Solution().encode("aaaaa") == "5[a]"

def test_example3():
    result = Solution().encode("aaaaaaaaaa")
    assert result == "10[a]"

def test_no_encoding_needed():
    assert Solution().encode("abcd") == "abcd"

def test_repeat_pattern():
    result = Solution().encode("abcabcabc")
    assert len(result) <= len("3[abc]")

def test_nested():
    result = Solution().encode("abababababab")
    assert len(result) <= len("6[ab]")

def test_mixed():
    result = Solution().encode("aabaabaab")
    assert len(result) <= len("3[aab]")

def test_single():
    assert Solution().encode("a") == "a"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
