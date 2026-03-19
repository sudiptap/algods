"""
2712. Minimum Cost to Make All Characters Equal
https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

Pattern: 19 - Linear DP (Greedy: at each boundary, flip shorter side)

---
APPROACH: At each position i where s[i] != s[i+1], we must flip either
the left portion [0..i] (cost i+1) or right portion [i+1..n-1] (cost n-i-1).
Always flip the shorter side.

Time: O(n)  Space: O(1)
---
"""


class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        cost = 0
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                cost += min(i + 1, n - i - 1)
        return cost


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumCost("0011") == 2
    assert sol.minimumCost("010101") == 9
    assert sol.minimumCost("0") == 0

    print("All tests passed!")
