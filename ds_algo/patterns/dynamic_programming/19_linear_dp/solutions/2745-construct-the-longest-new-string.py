"""
2745. Construct the Longest New String
https://leetcode.com/problems/construct-the-longest-new-string/

Pattern: 19 - Linear DP (Math)

---
APPROACH: We have x "AA", y "BB", z "AB" strings. "AB" can always be inserted.
"AA" and "BB" must alternate: ...AA BB AA BB... The count of usable AA/BB pairs
is min(x,y) if x==y, else min(x,y)+1 for the excess side. Plus all z "AB"s.

Time: O(1)  Space: O(1)
---
"""


class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # AA and BB alternate. We can use min(x,y) of each, plus 1 extra of whichever is larger.
        if x == y:
            return (2 * x + 2 * y + 2 * z)
        else:
            mn = min(x, y)
            return (2 * mn + 2 * (mn + 1) + 2 * z)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.longestString(2, 5, 1) == 12
    assert sol.longestString(3, 2, 2) == 14

    print("All tests passed!")
