"""
2060. Check if an Original String Exists Given Two Encoded Strings (Hard)
https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

Given two encoded strings s1 and s2 (mix of lowercase letters and digits
representing counts of wildcard characters), determine if there exists
an original string that both encodings could represent.

Pattern: LCS-style DP on (i, j, diff)
Approach:
- dp on (i, j, diff) where i = position in s1, j = position in s2,
  diff = number of unmatched characters (positive = s1 ahead, negative = s2 ahead).
- If both at letter positions and diff == 0: letters must match.
- If at digit, expand all possible numeric values (1, 2, or 3 digit numbers).
- Memoize (i, j, diff).

Time:  O(n1 * n2 * D) where D = range of diff values (bounded ~2000)
Space: O(n1 * n2 * D)
"""

from functools import lru_cache


class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        """Return True if both encoded strings could represent the same original.

        Args:
            s1: First encoded string.
            s2: Second encoded string.

        Returns:
            True if a common original string exists.
        """
        n1, n2 = len(s1), len(s2)

        @lru_cache(maxsize=None)
        def dp(i, j, diff):
            # diff > 0: s1 has diff more unmatched wildcard chars ahead
            # diff < 0: s2 has |diff| more unmatched wildcard chars ahead
            if i == n1 and j == n2:
                return diff == 0

            # If diff > 0: s1 is ahead, need to consume from s2
            if diff > 0:
                if j < n2:
                    if s2[j].isdigit():
                        # Parse numbers from s2
                        num = 0
                        for k in range(j, min(j + 3, n2)):
                            if not s2[k].isdigit():
                                break
                            num = num * 10 + int(s2[k])
                            if dp(i, k + 1, diff - num):
                                return True
                    else:
                        # s2 has a letter, consume one wildcard from diff
                        if dp(i, j + 1, diff - 1):
                            return True
                return False

            # If diff < 0: s2 is ahead, need to consume from s1
            if diff < 0:
                if i < n1:
                    if s1[i].isdigit():
                        num = 0
                        for k in range(i, min(i + 3, n1)):
                            if not s1[k].isdigit():
                                break
                            num = num * 10 + int(s1[k])
                            if dp(k + 1, j, diff + num):
                                return True
                    else:
                        if dp(i + 1, j, diff + 1):
                            return True
                return False

            # diff == 0
            if i < n1 and s1[i].isdigit():
                num = 0
                for k in range(i, min(i + 3, n1)):
                    if not s1[k].isdigit():
                        break
                    num = num * 10 + int(s1[k])
                    if dp(k + 1, j, diff + num):
                        return True
                return False

            if j < n2 and s2[j].isdigit():
                num = 0
                for k in range(j, min(j + 3, n2)):
                    if not s2[k].isdigit():
                        break
                    num = num * 10 + int(s2[k])
                    if dp(i, k + 1, diff - num):
                        return True
                return False

            # Both are letters
            if i < n1 and j < n2:
                if s1[i] == s2[j]:
                    return dp(i + 1, j + 1, 0)
                return False

            return False

        return dp(0, 0, 0)


# ---------- tests ----------
def test_possibly_equals():
    sol = Solution()

    # Example 1
    assert sol.possiblyEquals("internationalization", "i18n") is True

    # Example 2
    assert sol.possiblyEquals("l123e", "44") is True

    # Example 3
    assert sol.possiblyEquals("a5b", "c5b") is False

    # Example 4
    assert sol.possiblyEquals("112s", "g]]]]]]]", ) is False

    # Simple match
    assert sol.possiblyEquals("abc", "abc") is True

    # Simple mismatch
    assert sol.possiblyEquals("abc", "abd") is False

    print("All tests passed for 2060. Check if Original String Exists Given Two Encoded Strings")


if __name__ == "__main__":
    test_possibly_equals()
