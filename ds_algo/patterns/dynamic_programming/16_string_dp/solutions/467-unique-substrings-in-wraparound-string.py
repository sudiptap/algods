"""
467. Unique Substrings in Wraparound String (Medium)

Pattern: 16_string_dp
- Track the maximum length of a consecutive wraparound substring ending at each character.
- The answer is the sum of these max lengths across all 26 characters.

Approach:
- The wraparound string is "...zabcdefghijklmnopqrstuvwxyzabc...".
- Two characters are consecutive in the wraparound string if (ord(c2) - ord(c1)) % 26 == 1.
- Maintain `cur_len` tracking the current consecutive run length.
- For each character, record the max run length ending at that character in `max_len[c]`.
- The number of unique substrings ending at character c is max_len[c] (each length 1..max_len[c]
  gives a distinct substring). Summing over all characters avoids double counting because
  substrings ending at different characters are necessarily different, and for the same ending
  character we only count the longest run (which subsumes all shorter ones).

Complexity:
- Time:  O(n) single pass through the string
- Space: O(1) - only 26-entry dictionary
"""

from typing import List


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        max_len = {}  # max consecutive wraparound substring length ending at char c
        cur_len = 0

        for i, c in enumerate(s):
            if i > 0 and (ord(c) - ord(s[i - 1])) % 26 == 1:
                cur_len += 1
            else:
                cur_len = 1
            max_len[c] = max(max_len.get(c, 0), cur_len)

        return sum(max_len.values())


# ---------- Tests ----------
def test():
    sol = Solution()

    # Example 1: "a" -> unique substrings in wraparound: "a"
    assert sol.findSubstringInWraproundString("a") == 1

    # Example 2: "cac" -> "a", "c" (no consecutive wraparound pair)
    assert sol.findSubstringInWraproundString("cac") == 2

    # Example 3: "zab" -> "z","a","b","za","ab","zab" = 6
    assert sol.findSubstringInWraproundString("zab") == 6

    # Single repeating character
    assert sol.findSubstringInWraproundString("aaaa") == 1

    # Full alphabet
    s = "abcdefghijklmnopqrstuvwxyz"
    # substrings: 26 of len 1, 25 of len 2, ..., 1 of len 26 = 26*27/2 = 351
    assert sol.findSubstringInWraproundString(s) == 351

    # Wraparound test
    assert sol.findSubstringInWraproundString("za") == 3  # "z","a","za"

    print("All tests passed!")


if __name__ == "__main__":
    test()
