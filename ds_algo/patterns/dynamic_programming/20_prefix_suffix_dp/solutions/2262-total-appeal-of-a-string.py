"""
2262. Total Appeal of A String
https://leetcode.com/problems/total-appeal-of-a-string/

Pattern: 20 - Prefix/Suffix DP

---
APPROACH: Track last occurrence of each character
- For each position i, the appeal contribution of character s[i] is (i - last[s[i]]).
  This counts how many new substrings ending at i gain s[i] as a new distinct char.
- Maintain running sum of appeal of all substrings ending at i.
- Total appeal = sum of appeal contributions across all positions.

Time: O(n)  Space: O(1) (26 chars)
---
"""


class Solution:
    def appealSum(self, s: str) -> int:
        last = {}
        total = 0
        cur_appeal = 0  # sum of appeal of all substrings ending at current position

        for i, c in enumerate(s):
            # s[i] contributes to (i - last[c]) new substrings as a new distinct char
            cur_appeal += (i - last.get(c, -1))
            total += cur_appeal
            last[c] = i

        return total


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.appealSum("abbca") == 28
    assert sol.appealSum("code") == 20
    assert sol.appealSum("a") == 1
    assert sol.appealSum("aa") == 3
    assert sol.appealSum("ab") == 5

    print("all tests passed")
