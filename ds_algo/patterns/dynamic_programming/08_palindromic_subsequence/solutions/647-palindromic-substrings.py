"""
647. Palindromic Substrings (Medium)
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.
A substring is palindromic if it reads the same forward and backward.
Each single character is a palindromic substring.

Approach - Expand Around Centers:
    There are 2n - 1 possible centers for palindromes (n single-char
    centers and n-1 between-char centers). For each center, expand
    outward while characters match and count each valid expansion.

Time:  O(n^2) - each expansion is O(n), done for O(n) centers
Space: O(1)
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """Return the number of palindromic substrings in s.

        Expands around each of the 2n-1 possible centers, counting
        every palindrome found.

        Args:
            s: Input string, 1 <= len(s) <= 1000.

        Returns:
            Total count of palindromic substrings.
        """
        n = len(s)
        count = 0

        def expand(left: int, right: int) -> int:
            """Count palindromes by expanding outward from center."""
            total = 0
            while left >= 0 and right < n and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1
            return total

        for i in range(n):
            count += expand(i, i)      # Odd-length palindromes
            count += expand(i, i + 1)  # Even-length palindromes

        return count

    def countSubstrings_dp(self, s: str) -> int:
        """DP approach for reference.

        dp[i][j] = True if s[i..j] is a palindrome.

        Args:
            s: Input string.

        Returns:
            Total count of palindromic substrings.
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1

        return count


# --- Tests ---

def test_example1():
    sol = Solution()
    assert sol.countSubstrings("abc") == 3  # "a", "b", "c"

def test_example2():
    sol = Solution()
    assert sol.countSubstrings("aaa") == 6  # "a","a","a","aa","aa","aaa"

def test_single_char():
    sol = Solution()
    assert sol.countSubstrings("a") == 1

def test_even_palindrome():
    sol = Solution()
    # "a","b","b","a","bb","abba" = 6
    assert sol.countSubstrings("abba") == 6

def test_no_multi_char_palindromes():
    sol = Solution()
    assert sol.countSubstrings("abcd") == 4

def test_dp_matches_expand():
    sol = Solution()
    for s in ["abc", "aaa", "abba", "racecar", "abcd", "a"]:
        assert sol.countSubstrings(s) == sol.countSubstrings_dp(s)


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_single_char()
    test_even_palindrome()
    test_no_multi_char_palindromes()
    test_dp_matches_expand()
    print("All tests passed!")
