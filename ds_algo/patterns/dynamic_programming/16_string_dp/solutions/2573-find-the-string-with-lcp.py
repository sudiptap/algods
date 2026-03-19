"""
2573. Find the String with LCP
https://leetcode.com/problems/find-the-string-with-lcp/

Pattern: 16 - String DP

---
APPROACH: Greedy construction + verification
- Greedily assign smallest possible character to each position.
- If lcp[i][j] > 0, then s[i] == s[j]. Use union-find to group positions that
  must have the same character.
- Assign characters greedily (smallest first) to each group.
- Verify: recompute LCP from the constructed string and check it matches input.

Time: O(n^2)  Space: O(n^2)
---
"""

from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s = [''] * n
        c = 0  # current character index (0='a', 1='b', ...)

        for i in range(n):
            if s[i]:
                continue
            if c >= 26:
                return ""
            s[i] = chr(ord('a') + c)
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    s[j] = s[i]
            c += 1

        # Verify: recompute LCP and compare
        # lcp[i][j] should equal:
        #   0 if s[i] != s[j]
        #   lcp[i+1][j+1] + 1 if s[i] == s[j]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    expected = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)
                else:
                    expected = 0
                if lcp[i][j] != expected:
                    return ""

        return ''.join(s)


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.findTheString([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]) == "abab"
    assert sol.findTheString([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]) == "aaaa"
    assert sol.findTheString([[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]) == ""

    print("all tests passed")
