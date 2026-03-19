"""
3628. Maximum Number of Subsequences After One Inserting
https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

Pattern: 19 - Linear DP

---
APPROACH: Count contributions
- Given string text and pattern of length 2 (p[0], p[1]).
- Insert one character (either p[0] or p[1]) anywhere to maximize
  the number of subsequences matching pattern.
- If we insert p[0] at position i: adds count of p[1] to the right of i.
- If we insert p[1] at position i: adds count of p[0] to the left of i.
- Best insertion of p[0]: at the very beginning (all p[1]s are to the right).
- Best insertion of p[1]: at the very end (all p[0]s are to the left).
- Count original subsequences + max(count_p1, count_p0).

Time: O(n)  Space: O(1)
---
"""


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        p0, p1 = pattern[0], pattern[1]
        count_p0 = 0
        count_p1 = 0
        original = 0

        for c in text:
            if c == p1:
                original += count_p0
                count_p1 += 1
            if c == p0 and c != p1:
                count_p0 += 1
            elif c == p0:  # p0 == p1
                count_p0 += 1

        # Recount properly
        count_p0 = text.count(p0)
        count_p1 = text.count(p1)

        # Recompute original count
        original = 0
        cnt0 = 0
        for c in text:
            if c == p1:
                original += cnt0
            if c == p0:
                cnt0 += 1

        # Insert p[0] at start: gain count_p1 more subsequences
        # Insert p[1] at end: gain count_p0 more subsequences
        return original + max(count_p0, count_p1)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumSubsequenceCount("abdcdbc", "ac") == 4
    assert sol.maximumSubsequenceCount("aabb", "ab") == 6
    assert sol.maximumSubsequenceCount("aa", "aa") == 3  # original=1, insert a: +2=3

    print("All tests passed!")
