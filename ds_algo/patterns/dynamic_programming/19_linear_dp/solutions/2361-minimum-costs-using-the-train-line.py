"""
2361. Minimum Costs Using the Train Line
https://leetcode.com/problems/minimum-costs-using-the-train-line/

Pattern: 19 - Linear DP

---
APPROACH: Two states - regular and express line
- reg[i] = min cost to reach stop i on regular line
- exp[i] = min cost to reach stop i on express line
- Transitions:
  reg[i] = min(reg[i-1] + regular[i], exp[i-1] + expressCost + regular[i])
  exp[i] = min(exp[i-1] + express[i], reg[i-1] + express[i] + expressCost)
- Start on regular line at stop 0 (cost 0) or express (cost expressCost).
- Answer for each stop i: min(reg[i], exp[i])

Time: O(n)  Space: O(1)
---
"""

from typing import List


class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        ans = [0] * n

        reg = 0  # cost at previous stop on regular
        exp = expressCost  # cost at previous stop on express (need to switch first)

        for i in range(n):
            new_reg = min(reg + regular[i], exp + regular[i])
            new_exp = min(exp + express[i], reg + expressCost + express[i])
            reg, exp = new_reg, new_exp
            ans[i] = min(reg, exp)

        return ans


# ---------- Tests ----------
if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumCosts([1, 6, 9, 5], [5, 2, 3, 10], 8) == [1, 7, 14, 19]
    assert sol.minimumCosts([11, 5, 13], [7, 10, 6], 3) == [10, 15, 24]
    assert sol.minimumCosts([1], [1], 5) == [1]

    print("all tests passed")
