"""
1397. Find All Good Strings (Hard)
https://leetcode.com/problems/find-all-good-strings/

Problem:
    Given strings s1, s2 of length n and an evil string, count strings s
    of length n with s1 <= s <= s2 that do NOT contain evil as a substring.

Pattern: 16 - String DP

Approach:
    1. Digit DP + KMP failure function.
    2. Count strings <= s2 without evil, minus count of strings <= s1-1
       without evil (or count strings < s1).
    3. Use digit DP: dp(pos, kmp_state, is_tight) where kmp_state tracks
       how much of evil we've matched so far.
    4. If kmp_state == len(evil), the string contains evil, so skip.
    5. Use KMP failure function to compute transitions efficiently.

Complexity:
    Time:  O(n * m * 26) where m = len(evil)
    Space: O(n * m) for memoization
"""

from functools import lru_cache

MOD = 10**9 + 7


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        m = len(evil)

        # Build KMP failure function
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and evil[j] != evil[i]:
                j = fail[j - 1]
            if evil[j] == evil[i]:
                j += 1
            fail[i] = j

        # Precompute KMP transitions: given state j and char c, what's next state?
        # Do this on the fly or precompute
        def kmp_next(j, c):
            while j > 0 and evil[j] != c:
                j = fail[j - 1]
            if evil[j] == c:
                j += 1
            return j

        def count_le(s):
            """Count strings <= s of length n that don't contain evil."""
            @lru_cache(maxsize=None)
            def dp(pos, kmp_state, tight):
                if kmp_state == m:
                    return 0  # evil found
                if pos == n:
                    return 1  # valid string

                limit = ord(s[pos]) - ord('a') if tight else 25
                result = 0
                for c in range(0, limit + 1):
                    new_tight = tight and (c == limit)
                    new_kmp = kmp_next(kmp_state, chr(c + ord('a')))
                    result = (result + dp(pos + 1, new_kmp, new_tight)) % MOD
                return result

            ans = dp(0, 0, True)
            dp.cache_clear()
            return ans

        # count(s1..s2) = count(<=s2) - count(<=s1) + (s1 doesn't contain evil ? 1 : 0)
        # Check if s1 contains evil
        def contains_evil(s):
            j = 0
            for c in s:
                j = kmp_next(j, c)
                if j == m:
                    return True
            return False

        result = (count_le(s2) - count_le(s1) + (0 if contains_evil(s1) else 1)) % MOD
        return result


# ---------- tests ----------
def run_tests():
    sol = Solution()

    # Test 1
    assert sol.findGoodStrings(2, "aa", "da", "b") == 51, \
        f"Test 1 failed: {sol.findGoodStrings(2, 'aa', 'da', 'b')}"

    # Test 2
    assert sol.findGoodStrings(8, "leetcode", "leetgoes", "leet") == 0, \
        f"Test 2 failed: {sol.findGoodStrings(8, 'leetcode', 'leetgoes', 'leet')}"

    # Test 3
    assert sol.findGoodStrings(2, "gx", "gz", "x") == 2, \
        f"Test 3 failed: {sol.findGoodStrings(2, 'gx', 'gz', 'x')}"

    # Test 4: single char, exclude "a" from "a" to "z" = 25
    assert sol.findGoodStrings(1, "a", "z", "a") == 25, \
        f"Test 4 failed: {sol.findGoodStrings(1, 'a', 'z', 'a')}"

    print("All tests passed for 1397. Find All Good Strings!")


if __name__ == "__main__":
    run_tests()
